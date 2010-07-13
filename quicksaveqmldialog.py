# -*- coding: utf-8 -*-

#******************************************************************************
#
# QuickSaveQml
# ---------------------------------------------------------
# Save default QML with one click
#
# Copyright (C) 2009-2010 Maxim Dubinin (sim@gis-lab.info)
# and Alexander Bruy (alexander.bruy@gmail.com)
#
# This source is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# This code is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# A copy of the GNU General Public License is available on the World Wide Web
# at <http://www.gnu.org/copyleft/gpl.html>. You can also obtain it by writing
# to the Free Software Foundation, Inc., 59 Temple Place - Suite 330, Boston,
# MA 02111-1307, USA.
#
#******************************************************************************

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *
from qgis.gui import *

from quicksaveqmldialogbase import Ui_QuickSaveQmlDialog

class QuickSaveQmlDialog( QDialog, Ui_QuickSaveQmlDialog ):
  def __init__( self, iface ):
    QDialog.__init__( self )
    self.setupUi( self )
    self.iface = iface

    self.version = int( QGis.QGIS_VERSION[ 2 ] )
    if self.version > 4:
      self.mapLayers = self.iface.legendInterface().layers()
    else:
      self.mapLayers = QgsMapLayerRegistry.instance().mapLayers().values()

    QObject.connect( self.lvMapLayers, SIGNAL( "clicked( const QModelIndex & )" ), self.doSaveStylesButtonEnabled )
    QObject.connect( self.rbRasterLayers, SIGNAL( "toggled( bool )" ), self.doSaveStylesButtonEnabled )
    QObject.connect( self.rbVectorLayers, SIGNAL( "toggled( bool )" ), self.doSaveStylesButtonEnabled )

    self.loadMapLayers()
    self.rbVectorLayers.setChecked( True )

  def loadMapLayers( self ):
    layersNameList = QStringList()
    if self.version > 4:
      for i in range( len( self.mapLayers ) ):
        layersNameList.append( self.mapLayers[ i ].name() )
    else:
      self.dictLayers={}
      for i in range( len( self.mapLayers ) ):
        layersNameList.append( self.mapLayers[ i ].name() )
        self.dictLayers[ self.mapLayers[ i ].name() ] = i
      layersNameList.sort()

    self.lvMapLayers.setModel( QStringListModel( layersNameList, self ) )
    self.lvMapLayers.setSelectionMode( QAbstractItemView.ExtendedSelection )
    self.lvMapLayers.setEditTriggers( QAbstractItemView.NoEditTriggers )

    if self.lvMapLayers.model().rowCount() == 0:
      self.btnSelectAll.setEnabled( False )

  def on_rbRasterLayers_toggled( self, checked ):
    for i in range( len( self.mapLayers ) ):
      if self.version > 4:
        idx = self.lvMapLayers.model().index( i, 0 )
        layerName = self.lvMapLayers.model().data( idx, 0 ).toString()
        for j in range( len( self.mapLayers ) ):
          if self.mapLayers[j].name() == layerName:
            break
        if checked and ( self.mapLayers[i].type() != QgsMapLayer.VectorLayer ):
          self.lvMapLayers.setRowHidden( i, False )
        elif not checked and ( self.mapLayers[i].type() == QgsMapLayer.RasterLayer ):
          self.lvMapLayers.setRowHidden( i, True )
        else:
          self.lvMapLayers.setRowHidden( i, True )

      if checked and ( self.mapLayers[i].type() != QgsMapLayer.VectorLayer ):
        self.lvMapLayers.setRowHidden( i, False )
      elif not checked and ( self.mapLayers[i].type() == QgsMapLayer.RasterLayer ):
        self.lvMapLayers.setRowHidden( i, True )
      else:
        self.lvMapLayers.setRowHidden( i, True )

  def on_rbVectorLayers_toggled( self, checked ):
    for i in range( len( self.mapLayers ) ):
      if self.version > 4:
        idx = self.lvMapLayers.model().index( i, 0 )
        layerName = self.lvMapLayers.model().data( idx, 0 ).toString()
        for j in range( len( self.mapLayers ) ):
          if self.mapLayers[j].name() == layerName:
            break
        if checked and ( self.mapLayers[i].type() != QgsMapLayer.RasterLayer ):
          self.lvMapLayers.setRowHidden( i, False )
        elif not checked and ( self.mapLayers[i].type() == QgsMapLayer.VectorLayer ):
          self.lvMapLayers.setRowHidden( i, True )
        else:
          self.lvMapLayers.setRowHidden( i, True )

      if checked and ( self.mapLayers[i].type() != QgsMapLayer.RasterLayer ):
        self.lvMapLayers.setRowHidden( i, False )
      elif not checked and ( self.mapLayers[i].type() == QgsMapLayer.VectorLayer ):
        self.lvMapLayers.setRowHidden( i, True )
      else:
        self.lvMapLayers.setRowHidden( i, True )

  def doSaveStylesButtonEnabled( self ):
    if len( self.lvMapLayers.selectedIndexes() ) == 0:
      self.btnSaveStyles.setEnabled( False )
    else:
      self.btnSaveStyles.setEnabled( True )

  def myPluginMessage( self, msg, type ):
    if type == "information":
      QMessageBox.information(self, QApplication.translate("MultiQmlDlg", "Information"), msg )
    elif type == "critical":
      QMessageBox.critical(self, QApplication.translate("MultiQmlDlg", "Error"), msg )

  @pyqtSignature( "" )
  def on_btnClose_clicked(self):
    #self.writeSettings()
    self.close()

  #def closeEvent( self, event ):
  # for i in range( len( self.mapLayers ) ):
  #   os.remove( self.tmpQmlSrcList[i] )
  # event.accept()

  @pyqtSignature( "" )
  def on_btnSelectAll_clicked(self):
    self.lvMapLayers.selectAll()
    self.btnSelectAll.setEnabled( True )
    self.btnSaveStyles.setEnabled( True )

  @pyqtSignature( "" )
  def on_btnSaveStyles_clicked(self):
    def isRasterQml():
      qmlFile = open( self.fileNameStyle, "rb" )
      line = qmlFile.readline()
      result = False
      while line != "":
        if "<rasterproperties>" in line:
          result = True
          break
        line = qmlFile.readline()
      qmlFile.close()
      return result

    selected = self.lvMapLayers.selectedIndexes()
    for i in selected:
      if self.version > 4:
        layer = self.mapLayers[i.row()]
      else:
        layer = self.mapLayers[ self.dictLayers[ i.data().toString() ] ]

      message, isLoaded = layer.saveDefaultStyle()
      if not isLoaded:
        self.myPluginMessage( QApplication.translate( "MultiQmlDlg", "Unable to save qml style for layer \"%1\"\n%2." )\
          .arg( layer.name() ).arg( message ), "critical" )
