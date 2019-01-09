# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Setting_Dialog(object):
    def setupUi(self, Setting_Dialog):
        Setting_Dialog.setObjectName("Setting_Dialog")
        Setting_Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Setting_Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.bl_show = QtWidgets.QListView(Setting_Dialog)
        self.bl_show.setGeometry(QtCore.QRect(10, 10, 371, 191))
        self.bl_show.setObjectName("bl_show")
        self.addButton = QtWidgets.QPushButton(Setting_Dialog)
        self.addButton.setGeometry(QtCore.QRect(220, 210, 75, 23))
        self.addButton.setObjectName("addButton")
        self.removeButton = QtWidgets.QPushButton(Setting_Dialog)
        self.removeButton.setGeometry(QtCore.QRect(300, 210, 75, 23))
        self.removeButton.setObjectName("removeButton")
        self.bl_line = QtWidgets.QLineEdit(Setting_Dialog)
        self.bl_line.setGeometry(QtCore.QRect(10, 210, 201, 21))
        self.bl_line.setObjectName("bl_line")

        self.retranslateUi(Setting_Dialog)
        self.buttonBox.accepted.connect(Setting_Dialog.accept)
        self.buttonBox.rejected.connect(Setting_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Setting_Dialog)

    def retranslateUi(self, Setting_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Setting_Dialog.setWindowTitle(_translate("Setting_Dialog", "Dialog"))
        self.addButton.setText(_translate("Setting_Dialog", "Add"))
        self.removeButton.setText(_translate("Setting_Dialog", "Remove"))

