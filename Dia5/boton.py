#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class ButtonWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Botones")
        self.set_border_width(30)

        hbox = Gtk.Box(spacing=60)
        self.add(hbox)

        button = Gtk.Button.new_with_label("Click Uno")
        button.connect("clicked", self.on_click_me_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_label("Click Dos")
        button.connect("clicked", self.on_open_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_label("Cerrar")
        button.connect("clicked", self.on_close_clicked)
        hbox.pack_start(button, True, True, 0)

    def on_click_me_clicked(self, button):
        print("\"boton 1\" se dio click")

    def on_open_clicked(self, button):
        print("\"boton 2\" se dio click")

    def on_close_clicked(self, button):
        print("Cerrar Aplicacion")
        Gtk.main_quit()

win = ButtonWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
