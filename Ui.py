import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import gobject

class KeePassEntry(object):
    def __init__(self, app, entry):
        self.app = app
        self.name = entry['Name']
        self.login = entry['Login']
        self.uuid = entry['Uuid']
        self.password = entry['Password']


class PinWindow(Gtk.Window):

    def __init__(self, app, entries):
        Gtk.Window.__init__(self, title="KeepassHTTP Pinentry")
        self.entries = entries
        self.set_border_width(10)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        for entry in entries:
            button = Gtk.Button.new_with_label(entry['Name'])
            button.connect("clicked", self.on_entry_clicked)
            hbox.pack_start(button, True, True, 0)


    def on_entry_clicked(self, button):
        return self.get_password_by_name(button.get_label())

    def get_password_by_name(self, name):
        for entry in self.entries:
            if entry['Name'] == name:
                print("D " + entry['Password'])
                try:
                    sys.stdout.flush()
                except:
                    pass
                print("OK")
                try:
                    sys.stdout.flush()
                except:
                    pass
                Gtk.main_quit()
                self.destroy()
                return
        print("D ")
        try:
            sys.stdout.flush()
        except:
            pass
        self.destroy()
