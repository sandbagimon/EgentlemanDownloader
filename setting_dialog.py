# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 13:59:28 2019

@author: sandb
"""

from PyQt5.QtWidgets import QDialog, QApplication ,QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QIcon, QPixmap
from setting_ui import *
import os
import sys

class SettingForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Setting_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.ui.addButton.clicked.connect(self.add)
    def add(self):
        new_blacklist = str(self.ui.bl_line.text())
        
#        self.ui.Login_Button.clicked.connect(self.login)
#    def login(self):
#        username = str(self.ui.input_username.text())
#        password = str(self.ui.input_password.text())
#        cookies = get_dict_cookies(username,password)
#        if len(cookies) == 4:
#            self.ui.login_browser.append('Successfully obtained cookies!')
#            f= open('cookie.txt','w+')
#            f.write(str(cookies))
#            f.close()
#            self.accept()
#        else:
#            self.ui.login_browser.append('Failed to obtain cookies.. Check username and password again')
#        return cookies,username
if __name__=="__main__":
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    else: 
        print('QApplication instance already exists: %s' % str(app))

    w = SettingForm()
 #   w.show
    w.setWindowTitle("");
    w.setWindowIcon(QIcon('icon.png'))
    app.exec_()