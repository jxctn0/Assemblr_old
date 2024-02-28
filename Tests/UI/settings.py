import cairo
from configparser import ConfigParser
import gi
import os
import Connector # This is the file that contains the class that connects to the pi pico

gi.require_version("Gtk", "3.0")
gi.require_version("GtkSource", "4")
from gi.repository import Gtk, GtkSource, Pango


class SettingsWindow(Gtk.Window):
    def __init__(self, device):
        Gtk.Window.__init__(self, title="Settings")

        self.set_border_width(10)
        self.set_default_size(400, 300)

        notebook = Gtk.Notebook()
        self.add(notebook)

        self.create_appearance_tab(notebook)
        self.create_device_tab(notebook)
        self.create_language_tab(notebook)

    def create_device_tab(self, notebook):
        device_tab = Gtk.Box()
        device_tab.set_border_width(10)
        device_tab.add(Gtk.Label(label="Device settings"))
        notebook.append_page(device_tab, Gtk.Label(label="Device"))
        grid = Gtk.Grid()
        grid.set_column_spacing(5)
        grid.set_row_spacing(5)
        device_tab.add(grid)

        # Add Box to input an IP address and port, and a submit button to connect to the device
        ip_label = Gtk.Label(label="IP Address")
        grid.attach(ip_label, 0, 0, 1, 1)
        self.ip_entry = Gtk.Entry()
        grid.attach(self.ip_entry, 1, 0, 1, 1)

        port_label = Gtk.Label(label="Port")
        grid.attach(port_label, 0, 1, 1, 1)
        self.port_entry = Gtk.Entry()
        grid.attach(self.port_entry, 1, 1, 1, 1)

        connect_button = Gtk.Button(label="Connect")
        connect_button.connect("clicked", self.connect_to_device)
        grid.attach(connect_button, 0, 2, 2, 1)

        # Add Box to input a code to send to the device
        code_label = Gtk.Label(label="Code")
        grid.attach(code_label, 0, 3, 1, 1)
        self.code_entry = Gtk.Entry()
        grid.attach(self.code_entry, 1, 3, 1, 1)


    def create_language_tab(self, notebook):
        language_tab = Gtk.Box()
        language_tab.set_border_width(10)
        language_tab.add(Gtk.Label(label="Language settings"))
        notebook.append_page(language_tab, Gtk.Label(label="Language"))
        

    def create_appearance_tab(self, notebook):
        appearance_tab = Gtk.Box()
        appearance_tab.set_border_width(10)
        notebook.append_page(appearance_tab, Gtk.Label(label="Appearance"))
        grid = Gtk.Grid()
        grid.set_column_spacing(5)
        grid.set_row_spacing(5)
        appearance_tab.add(grid)

        font_label = Gtk.Label(label="Font")
        grid.attach(font_label, 0, 0, 1, 1)
        font_button = Gtk.FontButton()
        font_button.connect("font-set", self.set_font)
        grid.attach(font_button, 1, 0, 1, 1)

    def kill(self, widget):
        self.destroy()

def main():
    win = SettingsWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
    