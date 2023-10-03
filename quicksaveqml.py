# -*- coding: utf-8 -*-
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *
from qgis.core import *
from qgis.PyQt.QtCore import QTranslator, QCoreApplication

# инициализируем ресурсы Qt из файла resouces.py
from . import resources_rc
import os
from os import path

from . import quicksaveqmldialog
from .compat import map_layers
from . import about_dialog


class QuickSaveQml:

    def __init__(self, iface):
        """Initialize the class"""
        self.iface = iface
        self.plugin_dir = path.dirname(__file__)
        self._translator = None
        self.__init_translator()

    def initGui(self):
        self.action = QAction(QIcon(":/plugins/quicksaveqml/icon.png"), "Save default QML", self.iface.mainWindow())
        self.action.setStatusTip("Click to save qml file as default (with the same as a layer)")
        self.action.setWhatsThis("Save QML files as default")

        self.actionBatch = QAction(QIcon(":/plugins/quicksaveqml/batch_save.png"), "Save default QML (batch)",
                                   self.iface.mainWindow())
        self.actionBatch.setStatusTip("Click to save qml files as default (with the same as a layer)")
        self.actionBatch.setWhatsThis("Save QML files as default (batch)")

        self.actionAbout = QAction(
            self.tr("About"),
            self.iface.mainWindow()
        )

        self.action.triggered.connect(self.run)
        self.actionBatch.triggered.connect(self.runBatch)
        self.actionAbout.triggered.connect(self.about)

        self.iface.addToolBarIcon(self.action)
        self.iface.addToolBarIcon(self.actionBatch)
        self.iface.addPluginToMenu('&Quickly save default QML', self.action)
        self.iface.addPluginToMenu('&Quickly save default QML', self.actionBatch)
        self.iface.addPluginToMenu('&Quickly save default QML', self.actionAbout)

    def unload(self):
        self.iface.removePluginVectorMenu('&Quickly save default QML', self.action)
        self.iface.removePluginVectorMenu('&Quickly save default QML', self.actionBatch)
        self.iface.removePluginVectorMenu('&Quickly save default QML', self.actionAbout)
        self.iface.removeToolBarIcon(self.action)
        self.iface.removeToolBarIcon(self.actionBatch)

    def run(self):
        layersmap = map_layers()
        layerslist = []
        curLayer = self.iface.mapCanvas().currentLayer()
        if curLayer == None:
            QMessageBox.information(self.iface.mainWindow(), "Warning", "No layers selected")
            return
        curLayerName = curLayer.source()
        basename = os.path.splitext(str(curLayerName))[0]
        curLayerQMLName = basename + ".qml"
        curLayer.saveNamedStyle(curLayerQMLName)

    def runBatch(self):
        dlg = quicksaveqmldialog.QuickSaveQmlDialog(self.iface)
        dlg.exec_()

    def __init_translator(self):
        # initialize locale
        locale = QSettings().value('locale/userLocale')

        def add_translator(locale_path):
            if not path.exists(locale_path):
                return
            translator = QTranslator()
            translator.load(locale_path)
            QCoreApplication.installTranslator(translator)
            self._translator = translator  # Should be kept in memory

        add_translator(path.join(
            self.plugin_dir, 'i18n',
            'quicksaveqml_{}.qm'.format(locale, locale.upper())
        ))

    def tr(self, message):
        return QCoreApplication.translate(__class__.__name__, message)

    def about(self):
        dialog = about_dialog.AboutDialog(os.path.basename(self.plugin_dir))
        dialog.exec_()
