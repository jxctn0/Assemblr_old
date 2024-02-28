from logging import config
import cairo
from configparser import ConfigParser
import os
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GtkSource, Pango, Gdk
import Connector  # This is the file that contains the class that connects to the pi pico


class Editor(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="GTK Text Editor")
        self.set_default_size(800, 600)

        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.config = ConfigParser()
        try:
            self.config.read("config.json")
        except Exception as e:
            print("Couldn't read config file:", e)
            # Create a new default config file with default values:

            # Dialog box to try get the IP and port
            dialog = Gtk.Dialog(
                title="Enter IP and Port",
                transient_for=self,
                flags=0,
                buttons=(Gtk.STOCK_OK, Gtk.ResponseType.OK),
            )
            dialog.set_default_size(150, 100)

            box = dialog.get_content_area()
            ip_label = Gtk.Label(label="IP Address:")
            box.add(ip_label)
            ip_entry = Gtk.Entry()
            box.add(ip_entry)
            port_label = Gtk.Label(label="Port:")
            box.add(port_label)
            port_entry = Gtk.Entry()
            box.add(port_entry)
            dialog.add(box)
            dialog.show_all()
            dialog.run()
            dialog.destroy()

            config = {
                "device": {
                    "ip": "192.168.0.78",  # Replace this with the actual IP address of your Raspberry Pi Pico
                    "port": 12345,  # Choose a port number
                },
                "editor": {"font": ["Monospace", 12]},
            }
            

        self.create_menu()
        self.create_textview()
        self.create_statusbar()

        # Create a Device object and attempt to connect to the device
        self.device = Connector.Device(
            "Pi-Pico", self.config["device"]["ip"], int(self.config["device"]["port"])
        )
        try:
            self.device.connect()
        except Exception as e:
            print("An error occurred while connecting:", e)
            # Show a dialog box with the error message
            dialog = Gtk.MessageDialog(
                parent=self,
                flags=0,
                message_type=Gtk.MessageType.ERROR,
                buttons=Gtk.ButtonsType.OK,
                text=f'An error occurred while connecting to {self.config["device"]["ip"]}:{int(self.config["device"]["port"])}',
            )
            dialog.run()
            dialog.destroy()

    def create_menu(self):
        menubar = Gtk.MenuBar()

        file_menu = Gtk.Menu()
        file_menu_open = Gtk.MenuItem(label="Open")
        file_menu_open.connect("activate", self.on_open_clicked)
        file_menu.append(file_menu_open)
        file_menu_save = Gtk.MenuItem(label="Save")
        file_menu_save.connect("activate", self.on_save_clicked)
        file_menu.append(file_menu_save)

        edit_menu = Gtk.Menu()
        edit_menu_cut = Gtk.MenuItem(label="Cut")
        edit_menu_cut.connect("activate", self.on_cut_clicked)
        edit_menu.append(edit_menu_cut)
        edit_menu_copy = Gtk.MenuItem(label="Copy")
        edit_menu_copy.connect("activate", self.on_copy_clicked)
        edit_menu.append(edit_menu_copy)
        edit_menu_paste = Gtk.MenuItem(label="Paste")
        edit_menu_paste.connect("activate", self.on_paste_clicked)
        edit_menu.append(edit_menu_paste)

        run_menu = Gtk.Menu()

        about_menu = Gtk.Menu()
        about_menu_settings = Gtk.MenuItem(label="Settings")
        about_menu_settings.connect("activate", self.open_settings)

        about_menu.append(about_menu_settings)

        file_item = Gtk.MenuItem(label="File")
        file_item.set_submenu(file_menu)
        menubar.append(file_item)

        edit_item = Gtk.MenuItem(label="Edit")
        edit_item.set_submenu(edit_menu)
        menubar.append(edit_item)

        run_item = Gtk.MenuItem(label="Run")
        run_item.set_submenu(run_menu)
        menubar.append(run_item)

        about_item = Gtk.MenuItem(label="About")
        about_item.set_submenu(about_menu)
        menubar.append(about_item)

        self.grid.attach(menubar, 0, 0, 1, 1)

    def create_textview(self):
        self.textview = GtkSource.View()
        self.textview.set_name("mainEditor")
        self.textbuffer = self.textview.get_buffer()

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_hexpand(True)
        scrolled_window.set_vexpand(True)
        scrolled_window.add(self.textview)

        self.grid.attach(scrolled_window, 0, 1, 1, 1)

        self.textview.set_show_line_numbers(True)
        lang_manager = GtkSource.LanguageManager()
        lang = lang_manager.get_language("assembly")
        self.textbuffer.set_language(lang)
        self.textview.modify_font(Pango.FontDescription("Monospace 12"))

    def create_statusbar(self):
        statusbar = Gtk.Statusbar()
        self.grid.attach(statusbar, 0, 2, 1, 1)

    def on_open_clicked(self, widget):
        dialog = Gtk.FileChooserDialog(
            title="Please choose a file", parent=self, action=Gtk.FileChooserAction.OPEN
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN,
            Gtk.ResponseType.OK,
        )

        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            filename = dialog.get_filename()
            self.load_file(filename)
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def open_settings(self, widget):
        import settings

        settings.main()

    def on_save_clicked(self, widget):
        dialog = Gtk.FileChooserDialog(
            title="Please choose a file",
            parent=self,
            action=Gtk.FileChooserAction.SAVE,
            buttons=(
                Gtk.STOCK_CANCEL,
                Gtk.ResponseType.CANCEL,
                Gtk.STOCK_SAVE,
                Gtk.ResponseType.OK,
            ),
        )
        dialog.set_do_overwrite_confirmation(True)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            filename = dialog.get_filename()
            text = self.textbuffer.get_text(
                self.textbuffer.get_start_iter(), self.textbuffer.get_end_iter(), True
            )
            with open(filename, "w") as file:
                file.write(text)
        dialog.destroy()

    def on_cut_clicked(self, widget):
        self.textbuffer.cut_clipboard(Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD), True)

    def on_copy_clicked(self, widget):
        self.textbuffer.copy_clipboard(Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD))

    def on_paste_clicked(self, widget):
        self.textbuffer.paste_clipboard(Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD))

    def load_file(self, filename):
        with open(filename, "r") as f:
            text = f.read()
            self.textbuffer.set_text(text)


def main():
    win = Editor()
    win.connect("destroy", on_destroy)
    win.show_all()
    Gtk.main()


def on_destroy(widget, event):
    dialog = Gtk.MessageDialog(
        parent=widget,
        flags=Gtk.DialogFlags.MODAL,
        type=Gtk.MessageType.QUESTION,
        buttons=Gtk.ButtonsType.YES_NO,
        message_format="Are you sure you want to quit?",
    )
    response = dialog.run()
    dialog.destroy()
    if response == Gtk.ResponseType.YES:
        Gtk.main_quit()
    else:
        return True  # Prevents the window from closing


if __name__ == "__main__":
    main()
