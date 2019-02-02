# USAGE
# python motion_detector.py --conf conf.json

import gi
gi.require_version('Gtk', '3.0')
import argparse
import warnings
import json
from gi.repository import Gtk, Gdk
from motion_detector.detector_window import DetectorWindow
from motion_detector.detector import detect
import threading

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--conf", required=True,
                help="path to the JSON configuration file")
args = vars(ap.parse_args())

# filter warnings, load the configuration and initialize the Dropbox
warnings.filterwarnings("ignore")
conf = json.load(open(args["conf"]))

win = DetectorWindow(conf)
win.connect("destroy", Gtk.main_quit)
win.show_all()
win.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(0, 0, 0))
win.fullscreen()

detector_thread = threading.Thread(target=detect, args=([conf, win.update_image, win.set_backlight_timer]))
detector_thread.daemon = True

detector_thread.start()
Gtk.main()

