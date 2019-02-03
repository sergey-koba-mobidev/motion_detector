import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, GLib

class DetectorWindow(Gtk.Window):

    def __init__(self, conf):
        self.conf = conf
        Gtk.Window.__init__(self, title="Motion Detector")
        self.image = Gtk.Image()
        self.add(self.image)
        self.timer = GLib.timeout_add(self.conf["backlight_timer"], self.hide_image, None)
    
    def update_image(self, frame):
        h, w, d = frame.shape
        pixbuf = GdkPixbuf.Pixbuf.new_from_data(frame.tostring(), GdkPixbuf.Colorspace.RGB, False, 8, w, h, w*3, None, None)
        self.image.set_from_pixbuf(pixbuf.copy())

    def set_backlight_timer(self):
        self.image.show()
        if self.timer is not None:
            GLib.source_remove(self.timer)
            self.timer = None
        self.timer = GLib.timeout_add(self.conf["backlight_timer"], self.hide_image, None)

    def hide_image(self, user_data):
        if self.timer is not None:
            GLib.source_remove(self.timer)
            self.timer = None
        self.image.hide()
