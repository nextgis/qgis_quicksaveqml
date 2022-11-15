# -*- coding: utf-8 -*-
def classFactory(iface):
  from .quicksaveqml import QuickSaveQml
  return QuickSaveQml(iface)
