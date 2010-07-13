# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quicksaveqmldialogbase.ui'
#
# Created: Mon Jul 12 21:50:59 2010
#      by: PyQt4 UI code generator 4.5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_QuickSaveQmlDialog(object):
    def setupUi(self, QuickSaveQmlDialog):
        QuickSaveQmlDialog.setObjectName("QuickSaveQmlDialog")
        QuickSaveQmlDialog.resize(217, 227)
        self.gridLayout = QtGui.QGridLayout(QuickSaveQmlDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(QuickSaveQmlDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lvMapLayers = QtGui.QListView(QuickSaveQmlDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lvMapLayers.sizePolicy().hasHeightForWidth())
        self.lvMapLayers.setSizePolicy(sizePolicy)
        self.lvMapLayers.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lvMapLayers.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.lvMapLayers.setObjectName("lvMapLayers")
        self.gridLayout.addWidget(self.lvMapLayers, 1, 0, 3, 1)
        self.groupBox = QtGui.QGroupBox(QuickSaveQmlDialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rbRasterLayers = QtGui.QRadioButton(self.groupBox)
        self.rbRasterLayers.setChecked(False)
        self.rbRasterLayers.setObjectName("rbRasterLayers")
        self.verticalLayout.addWidget(self.rbRasterLayers)
        self.rbVectorLayers = QtGui.QRadioButton(self.groupBox)
        self.rbVectorLayers.setObjectName("rbVectorLayers")
        self.verticalLayout.addWidget(self.rbVectorLayers)
        self.gridLayout.addWidget(self.groupBox, 1, 1, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnSelectAll = QtGui.QPushButton(QuickSaveQmlDialog)
        self.btnSelectAll.setObjectName("btnSelectAll")
        self.verticalLayout_2.addWidget(self.btnSelectAll)
        self.btnSaveStyles = QtGui.QPushButton(QuickSaveQmlDialog)
        self.btnSaveStyles.setObjectName("btnSaveStyles")
        self.verticalLayout_2.addWidget(self.btnSaveStyles)
        self.btnClose = QtGui.QPushButton(QuickSaveQmlDialog)
        self.btnClose.setObjectName("btnClose")
        self.verticalLayout_2.addWidget(self.btnClose)
        self.gridLayout.addLayout(self.verticalLayout_2, 3, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)

        self.retranslateUi(QuickSaveQmlDialog)
        QtCore.QMetaObject.connectSlotsByName(QuickSaveQmlDialog)

    def retranslateUi(self, QuickSaveQmlDialog):
        QuickSaveQmlDialog.setWindowTitle(QtGui.QApplication.translate("QuickSaveQmlDialog", "Quick save QML", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("QuickSaveQmlDialog", "Layers:", None, QtGui.QApplication.UnicodeUTF8))
        self.rbRasterLayers.setText(QtGui.QApplication.translate("QuickSaveQmlDialog", "Raster", None, QtGui.QApplication.UnicodeUTF8))
        self.rbVectorLayers.setText(QtGui.QApplication.translate("QuickSaveQmlDialog", "Vector", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSelectAll.setText(QtGui.QApplication.translate("QuickSaveQmlDialog", "Select all", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSaveStyles.setText(QtGui.QApplication.translate("QuickSaveQmlDialog", "Save style(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClose.setText(QtGui.QApplication.translate("QuickSaveQmlDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

