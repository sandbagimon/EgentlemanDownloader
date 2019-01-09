# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login_Dialog(object):
    def setupUi(self, Login_Dialog):
        Login_Dialog.setObjectName("Login_Dialog")
        Login_Dialog.resize(374, 271)
        self.login_browser = QtWidgets.QTextBrowser(Login_Dialog)
        self.login_browser.setGeometry(QtCore.QRect(10, 180, 191, 81))
        self.login_browser.setObjectName("login_browser")
        self.input_username = QtWidgets.QLineEdit(Login_Dialog)
        self.input_username.setGeometry(QtCore.QRect(70, 50, 201, 21))
        self.input_username.setObjectName("input_username")
        self.input_password = QtWidgets.QLineEdit(Login_Dialog)
        self.input_password.setGeometry(QtCore.QRect(70, 90, 201, 21))
        self.input_password.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.input_password.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password.setObjectName("input_password")
        self.label = QtWidgets.QLabel(Login_Dialog)
        self.label.setGeometry(QtCore.QRect(10, 50, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Login_Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 51, 16))
        self.label_2.setObjectName("label_2")
        self.Login_Button = QtWidgets.QPushButton(Login_Dialog)
        self.Login_Button.setGeometry(QtCore.QRect(250, 200, 75, 23))
        self.Login_Button.setObjectName("Login_Button")

        self.retranslateUi(Login_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Login_Dialog)

    def retranslateUi(self, Login_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Login_Dialog.setWindowTitle(_translate("Login_Dialog", "Dialog"))
        self.label.setText(_translate("Login_Dialog", "Username"))
        self.label_2.setText(_translate("Login_Dialog", "Password"))
        self.Login_Button.setText(_translate("Login_Dialog", "Log In"))

