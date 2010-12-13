# -*- coding: utf-8 -*-
mVersion = "0.1.1"
def name():
  return "Quickly save default qml"
def description():
  return "Save default QML with one click"
def qgisMinimumVersion():
  return "1.0"
def version():
  return mVersion
def authorName():
  return "Maxim Dubinin (sim@gis-lab.info)"
def icon():
  return "icon.png"
def classFactory(iface):
  from quicksaveqml import QuickSaveQml
  return QuickSaveQml(iface)
