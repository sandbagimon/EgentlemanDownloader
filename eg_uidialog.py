# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(921, 523)
        self.connect_button = QtWidgets.QPushButton(Dialog)
        self.connect_button.setEnabled(False)
        self.connect_button.setGeometry(QtCore.QRect(490, 80, 75, 23))
        self.connect_button.setObjectName("connect_button")
        self.setting_button = QtWidgets.QPushButton(Dialog)
        self.setting_button.setGeometry(QtCore.QRect(490, 10, 75, 23))
        self.setting_button.setObjectName("setting_button")
        self.search_button = QtWidgets.QPushButton(Dialog)
        self.search_button.setEnabled(False)
        self.search_button.setGeometry(QtCore.QRect(410, 10, 75, 23))
        self.search_button.setDefault(True)
        self.search_button.setObjectName("search_button")
        self.login_button = QtWidgets.QPushButton(Dialog)
        self.login_button.setGeometry(QtCore.QRect(410, 80, 75, 23))
        self.login_button.setObjectName("login_button")
        self.download_button = QtWidgets.QPushButton(Dialog)
        self.download_button.setEnabled(False)
        self.download_button.setGeometry(QtCore.QRect(520, 470, 75, 23))
        self.download_button.setObjectName("download_button")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(200, 100, 161, 311))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(6, 0, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.frame_2)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 70, 161, 221))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_2.setGeometry(QtCore.QRect(60, 290, 16, 20))
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(380, 100, 161, 311))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(6, 0, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.frame_3)
        self.graphicsView_3.setGeometry(QtCore.QRect(0, 70, 161, 221))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_3.setGeometry(QtCore.QRect(60, 290, 16, 17))
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.frame_4 = QtWidgets.QFrame(Dialog)
        self.frame_4.setGeometry(QtCore.QRect(560, 100, 161, 311))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.frame_4)
        self.graphicsView_4.setGeometry(QtCore.QRect(0, 70, 161, 221))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_4.setGeometry(QtCore.QRect(70, 290, 16, 17))
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.nextpage_button = QtWidgets.QPushButton(Dialog)
        self.nextpage_button.setGeometry(QtCore.QRect(520, 420, 75, 23))
        self.nextpage_button.setObjectName("nextpage_button")
        self.pervpage_button = QtWidgets.QPushButton(Dialog)
        self.pervpage_button.setGeometry(QtCore.QRect(20, 420, 75, 23))
        self.pervpage_button.setObjectName("pervpage_button")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 50, 592, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.doujinshi_cb = QtWidgets.QCheckBox(self.layoutWidget)
        self.doujinshi_cb.setObjectName("doujinshi_cb")
        self.horizontalLayout.addWidget(self.doujinshi_cb)
        self.manga_cb = QtWidgets.QCheckBox(self.layoutWidget)
        self.manga_cb.setObjectName("manga_cb")
        self.horizontalLayout.addWidget(self.manga_cb)
        self.artist_cb = QtWidgets.QCheckBox(self.layoutWidget)
        self.artist_cb.setObjectName("artist_cb")
        self.horizontalLayout.addWidget(self.artist_cb)
        self.game_cb = QtWidgets.QCheckBox(self.layoutWidget)
        self.game_cb.setObjectName("game_cb")
        self.horizontalLayout.addWidget(self.game_cb)
        self.western_cb = QtWidgets.QCheckBox(self.layoutWidget)
        self.western_cb.setObjectName("western_cb")
        self.horizontalLayout.addWidget(self.western_cb)
        self.nonh_cb = QtWidgets.QCheckBox(self.layoutWidget)
        self.nonh_cb.setObjectName("nonh_cb")
        self.horizontalLayout.addWidget(self.nonh_cb)
        self.image_cb = QtWidgets.QCheckBox(self.layoutWidget)
        self.image_cb.setObjectName("image_cb")
        self.horizontalLayout.addWidget(self.image_cb)
        self.cosplay_cb = QtWidgets.QCheckBox(self.layoutWidget)
        self.cosplay_cb.setObjectName("cosplay_cb")
        self.horizontalLayout.addWidget(self.cosplay_cb)
        self.asia_cb = QtWidgets.QCheckBox(Dialog)
        self.asia_cb.setGeometry(QtCore.QRect(10, 70, 68, 17))
        self.asia_cb.setObjectName("asia_cb")
        self.misc_cb = QtWidgets.QCheckBox(Dialog)
        self.misc_cb.setGeometry(QtCore.QRect(90, 70, 68, 17))
        self.misc_cb.setObjectName("misc_cb")
        self.frame_1 = QtWidgets.QFrame(Dialog)
        self.frame_1.setGeometry(QtCore.QRect(20, 100, 161, 311))
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.label_1 = QtWidgets.QLabel(self.frame_1)
        self.label_1.setGeometry(QtCore.QRect(6, 0, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_1.setFont(font)
        self.label_1.setText("")
        self.label_1.setWordWrap(True)
        self.label_1.setObjectName("label_1")
        self.graphicsView_1 = QtWidgets.QGraphicsView(self.frame_1)
        self.graphicsView_1.setGeometry(QtCore.QRect(0, 70, 161, 221))
        self.graphicsView_1.setObjectName("graphicsView_1")
        self.checkBox_1 = QtWidgets.QCheckBox(self.frame_1)
        self.checkBox_1.setGeometry(QtCore.QRect(50, 290, 16, 17))
        self.checkBox_1.setText("")
        self.checkBox_1.setObjectName("checkBox_1")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(120, 410, 361, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.keywords_entry = QtWidgets.QLineEdit(Dialog)
        self.keywords_entry.setGeometry(QtCore.QRect(10, 10, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.keywords_entry.setFont(font)
        self.keywords_entry.setTabletTracking(False)
        self.keywords_entry.setDragEnabled(False)
        self.keywords_entry.setObjectName("keywords_entry")
        self.frame_5 = QtWidgets.QFrame(Dialog)
        self.frame_5.setGeometry(QtCore.QRect(740, 100, 161, 311))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.graphicsView_5 = QtWidgets.QGraphicsView(self.frame_5)
        self.graphicsView_5.setGeometry(QtCore.QRect(0, 70, 161, 221))
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.checkBox_5 = QtWidgets.QCheckBox(self.frame_5)
        self.checkBox_5.setGeometry(QtCore.QRect(70, 290, 16, 17))
        self.checkBox_5.setText("")
        self.checkBox_5.setObjectName("checkBox_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.connect_button.setText(_translate("Dialog", "Connect"))
        self.setting_button.setText(_translate("Dialog", "Setting"))
        self.search_button.setText(_translate("Dialog", "Search"))
        self.login_button.setText(_translate("Dialog", "Log In"))
        self.download_button.setText(_translate("Dialog", "DownLoad"))
        self.nextpage_button.setText(_translate("Dialog", "Next Page"))
        self.pervpage_button.setText(_translate("Dialog", "Perv. Page"))
        self.doujinshi_cb.setText(_translate("Dialog", "Doujinshi"))
        self.manga_cb.setText(_translate("Dialog", "Manga"))
        self.artist_cb.setText(_translate("Dialog", "Artist CG"))
        self.game_cb.setText(_translate("Dialog", "Game CG"))
        self.western_cb.setText(_translate("Dialog", "Western"))
        self.nonh_cb.setText(_translate("Dialog", "Non-H"))
        self.image_cb.setText(_translate("Dialog", "Image set"))
        self.cosplay_cb.setText(_translate("Dialog", "Cosplay"))
        self.asia_cb.setText(_translate("Dialog", "Asia"))
        self.misc_cb.setText(_translate("Dialog", "Misc"))
        self.keywords_entry.setPlaceholderText(_translate("Dialog", "请输入搜索内容/ Keywords"))
