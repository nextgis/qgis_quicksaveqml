# -*- coding: utf-8 -*-
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *
from qgis.core import *

# инициализируем ресурсы Qt из файла resouces.py
from . import resources_rc
import os
from pathlib import Path

from . import quicksaveqmldialog
from . import aboutdialog
from .compat import map_layers


class QuickSaveQml:
    def __init__(self, iface):
        """Initialize the class"""
        self.iface = iface

    def initGui(self):
        self.action = QAction(
            QIcon(":/plugins/quicksaveqml/icons/icon.png"),
            "Save default QML",
            self.iface.mainWindow(),
        )
        self.action.setStatusTip(
            "Click to save qml file as default (with the same as a layer)"
        )
        self.action.setWhatsThis("Save QML files as default")

        self.actionBatch = QAction(
            QIcon(":/plugins/quicksaveqml/icons/batch_save.png"),
            "Save default QML (batch)",
            self.iface.mainWindow(),
        )
        self.actionBatch.setStatusTip(
            "Click to save qml files as default (with the same as a layer)"
        )
        self.actionBatch.setWhatsThis("Save QML files as default (batch)")

        self.actionAbout = QAction(
            QIcon(":/plugins/quicksaveqml/icons/about.png"),
            "About...",
            self.iface.mainWindow(),
        )

        self.action.triggered.connect(self.run)
        self.actionBatch.triggered.connect(self.runBatch)
        self.actionAbout.triggered.connect(self.about)

        self.iface.addToolBarIcon(self.action)
        self.iface.addToolBarIcon(self.actionBatch)

        self.iface.addPluginToMenu("Save default QML", self.action)
        self.iface.addPluginToMenu("Save default QML", self.actionBatch)
        self.iface.addPluginToMenu("Save default QML", self.actionAbout)

        self.__show_help_action = QAction(
            QIcon(":/plugins/quicksaveqml/icons/icon.png"),
            "Quickly save default QML",
        )
        self.__show_help_action.triggered.connect(self.about)
        plugin_help_menu = self.iface.pluginHelpMenu()
        assert plugin_help_menu is not None
        plugin_help_menu.addAction(self.__show_help_action)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        self.iface.removeToolBarIcon(self.actionBatch)

        self.iface.removePluginMenu("Save default QML", self.action)
        self.iface.removePluginMenu("Save default QML", self.actionBatch)
        self.iface.removePluginMenu("Save default QML", self.actionAbout)

    def run(self):
        layersmap = map_layers()
        layerslist = []
        curLayer = self.iface.mapCanvas().currentLayer()
        if curLayer == None:
            QMessageBox.information(
                self.iface.mainWindow(), "Warning", "No layers selected"
            )
            return
        curLayerName = curLayer.source()
        basename = os.path.splitext(str(curLayerName))[0]
        curLayerQMLName = basename + ".qml"
        curLayer.saveNamedStyle(curLayerQMLName)

    def runBatch(self):
        dlg = quicksaveqmldialog.QuickSaveQmlDialog(self.iface)
        dlg.exec()

    def about(self):
        package_name = str(Path(__file__).parent.name)
        dlg = aboutdialog.AboutDialog(package_name)
        dlg.exec()
