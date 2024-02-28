import unittest
from gi.repository import Gtk, GtkSource

from ui import TextViewWindow


class TestTextViewWindow(unittest.TestCase):
    def setUp(self):
        self.window = TextViewWindow()

    def test_create_menu(self):
        self.assertIsInstance(self.window.grid.get_child_at(0, 0), Gtk.MenuBar)

    def test_create_textview(self):
        self.assertIsInstance(self.window.textview, GtkSource.View)
        self.assertIsInstance(self.window.textbuffer, GtkSource.Buffer)

    def test_create_statusbar(self):
        self.assertIsInstance(self.window.grid.get_child_at(0, 2), Gtk.Statusbar)

    def test_on_open_clicked(self):
        # TODO: Write test case for on_open_clicked method
        pass

    def test_open_settings(self):
        # TODO: Write test case for open_settings method
        pass

    def test_load_file(self):
        # TODO: Write test case for load_file method
        pass

    def tearDown(self):
        self.window.destroy()


if __name__ == "__main__":
    unittest.main()