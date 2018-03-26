import sys, gi

from lib import submanga, heavenmanga
from urllib.parse import urlparse

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def onButtonPressed(self, button):
        uri    = builder.get_object('entry1').get_text()
        site   = urlparse(uri).netloc.replace("www.", "")
        domain = site.split('.')[0]

        output = builder.get_object('filechooserbutton1').get_filename()

        websites = {
            'submanga': submanga,
            #'tumangaonline': tumangaonline,
            'heavenmanga': heavenmanga,
        }

        try:
            websites[domain].getChapter(uri, dest=output)

        except AttributeError as ae:
            print(ae)
            print("Error: '{}' is not a valid URL!".format(uri))
        except KeyError:
            print("Ooops! Sorry, '{}' is not a valid URL or is not supported yet.".format(site))

builder = Gtk.Builder()
builder.add_from_file("gui.glade")
builder.connect_signals(Handler())

window = builder.get_object("manga-dl")
window.show_all()

Gtk.main()