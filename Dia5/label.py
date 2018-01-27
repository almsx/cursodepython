#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class LabelWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Campos de Texto")
        
        hbox = Gtk.Box(spacing=10)
        hbox.set_homogeneous(False)
        vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=30)
        vbox_left.set_homogeneous(False)
        vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=30)
        vbox_right.set_homogeneous(False)
        
        hbox.pack_start(vbox_left, True, True, 0)
        hbox.pack_start(vbox_right, True, True, 0)
        
        label = Gtk.Label("Etiqueta Normal")
        vbox_left.pack_start(label, True, True, 0)
        
        label = Gtk.Label()
        label.set_text("Etiquetas de texto en.\nmultiples lineas justificado a la izquierda.")
        label.set_justify(Gtk.Justification.LEFT)
        vbox_left.pack_start(label, True, True, 0)
        
        label = Gtk.Label(
            "Etiqueta a la derecha.\nCon multiples lineas.")
        label.set_justify(Gtk.Justification.RIGHT)
        vbox_left.pack_start(label, True, True, 0)
        
        label = Gtk.Label("Lorem Ipsum es simplemente el texto de relleno de las imprentas "
                          " y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las"
                          "industrias desde el año 1500, cuando un impresor (N. del T. persona "
                          "que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló"
                          "de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió "
                          "500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos,"
                          "quedando esencialmente igual al original. Fue popularizado en los 60s con la"
                          "creación de las hojas 'Letraset', las cuales contenian pasajes de"
                          "Lorem Ipsum, y más recientemente con software de autoedición, como por "
                          "ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum.")
        label.set_line_wrap(True)
        label.set_justify(Gtk.Justification.FILL)
        vbox_right.pack_start(label, True, True, 0)

        
        self.add(hbox)

window = LabelWindow()        
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()