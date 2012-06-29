# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

# инициализируем ресурсы Qt из файла resouces.py
import resources_rc
import os

import quicksaveqmldialog

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

    QObject.connect( self.action, SIGNAL( "triggered()" ), self.run )
    QObject.connect( self.actionBatch, SIGNAL( "triggered()" ), self.runBatch )

    self.iface.addToolBarIcon( self.action )
    self.iface.addToolBarIcon( self.actionBatch )

  def unload( self ):
    self.iface.removeToolBarIcon( self.action )
    self.iface.removeToolBarIcon( self.actionBatch )

  def run( self ):
    layersmap=QgsMapLayerRegistry.instance().mapLayers()
    layerslist=[]
    curLayer = self.iface.mapCanvas().currentLayer()
    if curLayer == None:
      infoString = QString( "No layers selected" )
      QMessageBox.information( self.iface.mainWindow(), "Warning", infoString )
      return
    curLayerName = curLayer.source()
    basename = os.path.splitext( unicode( curLayerName ) )[ 0 ]
    curLayerQMLName = basename + ".qml"
    curLayer.saveNamedStyle( curLayerQMLName )

  def runBatch( self ):
    dlg = quicksaveqmldialog.QuickSaveQmlDialog( self.iface )
    dlg.exec_()
