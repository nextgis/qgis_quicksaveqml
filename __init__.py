# -*- coding: utf-8 -*-
mVersion = "0.1.5"
def name():
  return "Quickly save default qml"
def description():
  return "Save default QML with one click"
def category():
  return "Plugins"
def qgisMinimumVersion():
  return "2.0.0"
def version():
  return "0.1.5"
def authorName():
  return "Maxim Dubinin (NextGIS)"
def icon():
  return "icon.png"
def classFactory(iface):
  from .quicksaveqml import QuickSaveQml
  return QuickSaveQml(iface)
