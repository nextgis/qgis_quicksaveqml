# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quicksaveqmldialogbase.ui'
#
# Created: Fri Jun 29 12:12:22 2012
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from qgis.PyQt import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_QuickSaveQmlDialog(object):
    def setupUi(self, QuickSaveQmlDialog):
        QuickSaveQmlDialog.setObjectName(_fromUtf8("QuickSaveQmlDialog"))
        QuickSaveQmlDialog.resize(217, 227)
        self.gridLayout = QtWidgets.QGridLayout(QuickSaveQmlDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtWidgets.QLabel(QuickSaveQmlDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lvMapLayers = QtWidgets.QListView(QuickSaveQmlDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lvMapLayers.sizePolicy().hasHeightForWidth())
        self.lvMapLayers.setSizePolicy(sizePolicy)
        self.lvMapLayers.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lvMapLayers.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.lvMapLayers.setObjectName(_fromUtf8("lvMapLayers"))
        self.gridLayout.addWidget(self.lvMapLayers, 1, 0, 3, 1)
        self.groupBox = QtWidgets.QGroupBox(QuickSaveQmlDialog)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.rbRasterLayers = QtWidgets.QRadioButton(self.groupBox)
        self.rbRasterLayers.setChecked(False)
        self.rbRasterLayers.setObjectName(_fromUtf8("rbRasterLayers"))
        self.verticalLayout.addWidget(self.rbRasterLayers)
        self.rbVectorLayers = QtWidgets.QRadioButton(self.groupBox)
        self.rbVectorLayers.setObjectName(_fromUtf8("rbVectorLayers"))
        self.verticalLayout.addWidget(self.rbVectorLayers)
        self.gridLayout.addWidget(self.groupBox, 1, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.btnSelectAll = QtWidgets.QPushButton(QuickSaveQmlDialog)
        self.btnSelectAll.setObjectName(_fromUtf8("btnSelectAll"))
        self.verticalLayout_2.addWidget(self.btnSelectAll)
        self.btnSaveStyles = QtWidgets.QPushButton(QuickSaveQmlDialog)
        self.btnSaveStyles.setObjectName(_fromUtf8("btnSaveStyles"))
        self.verticalLayout_2.addWidget(self.btnSaveStyles)
        self.btnClose = QtWidgets.QPushButton(QuickSaveQmlDialog)
        self.btnClose.setObjectName(_fromUtf8("btnClose"))
        self.verticalLayout_2.addWidget(self.btnClose)
        self.gridLayout.addLayout(self.verticalLayout_2, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)

        self.retranslateUi(QuickSaveQmlDialog)
        QtCore.QMetaObject.connectSlotsByName(QuickSaveQmlDialog)

    def retranslateUi(self, QuickSaveQmlDialog):
        QuickSaveQmlDialog.setWindowTitle(QtWidgets.QApplication.translate("QuickSaveQmlDialog", "Quick save QML", None))
        self.label.setText(QtWidgets.QApplication.translate("QuickSaveQmlDialog", "Layers:", None))
        self.rbRasterLayers.setText(QtWidgets.QApplication.translate("QuickSaveQmlDialog", "Raster", None))
        self.rbVectorLayers.setText(QtWidgets.QApplication.translate("QuickSaveQmlDialog", "Vector", None))
        self.btnSelectAll.setText(QtWidgets.QApplication.translate("QuickSaveQmlDialog", "Select all", None))
        self.btnSaveStyles.setText(QtWidgets.QApplication.translate("QuickSaveQmlDialog", "Save style(s)", None))
        self.btnClose.setText(QtWidgets.QApplication.translate("QuickSaveQmlDialog", "Close", None))

