# -*- coding: utf-8 -*-
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *
from qgis.core import *

# инициализируем ресурсы Qt из файла resouces.py
from . import resources_rc
import os

from . import quicksaveqmldialog
from .compat import map_layers

class QuickSaveQml:

  def __init__( self, iface ):
    """Initialize the class"""
    self.iface = iface

  def initGui( self ):
    self.action = QAction( QIcon( ":/plugins/quicksaveqml/icon.png"), "Save default QML", self.iface.mainWindow() )
    self.action.setStatusTip( "Click to save qml file as default (with the same as a layer)" )
    self.action.setWhatsThis( "Save QML files as default" )

    self.actionBatch = QAction(QIcon( ":/plugins/quicksaveqml/batch_save.png" ), "Save default QML (batch)", self.iface.mainWindow() )
    self.actionBatch.setStatusTip( "Click to save qml files as default (with the same as a layer)" )
    self.actionBatch.setWhatsThis( "Save QML files as default (batch)" )

    self.action.triggered.connect(self.run)
    self.actionBatch.triggered.connect(self.runBatch)

    self.iface.addToolBarIcon( self.action )
    self.iface.addToolBarIcon( self.actionBatch )

  def unload( self ):
    self.iface.removeToolBarIcon( self.action )
    self.iface.removeToolBarIcon( self.actionBatch )

  def run( self ):
    layersmap = map_layers()
    layerslist = []
    curLayer = self.iface.mapCanvas().currentLayer()
    if curLayer == None:
      QMessageBox.information( self.iface.mainWindow(), "Warning", "No layers selected" )
      return
    curLayerName = curLayer.source()
    basename = os.path.splitext( str( curLayerName ) )[ 0 ]
    curLayerQMLName = basename + ".qml"
    curLayer.saveNamedStyle( curLayerQMLName )

  def runBatch( self ):
    dlg = quicksaveqmldialog.QuickSaveQmlDialog( self.iface )
    dlg.exec_()
