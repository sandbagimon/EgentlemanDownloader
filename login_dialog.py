# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 18:12:10 2019

@author: sandb
"""

from PyQt5.QtWidgets import QDialog, QApplication ,QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QIcon, QPixmap
from login_ui import *
from test_login import *
import sys

class LoginForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login_Dialog()
        self.ui.setupUi(self)
        self.show()
        
        self.ui.Login_Button.clicked.connect(self.login)
    def login(self):
        username = str(self.ui.input_username.text())
        password = str(self.ui.input_password.text())
        cookies = get_dict_cookies(username,password)
        if len(cookies) == 4:
            self.ui.login_browser.append('Successfully obtained cookies!')
            f= open('cookie.txt','w+')
            f.write(str(cookies))
            f.close()
            self.accept()
        else:
            self.ui.login_browser.append('Failed to obtain cookies.. Check username and password again')
        return cookies,username
#if __name__=="__main__":
#    app = QApplication.instance()
#    if app is None:
#        app = QApplication(sys.argv)
#    else: 
#        print('QApplication instance already exists: %s' % str(app))
#
#    w = LoginForm()
# #   w.show
#    w.setWindowTitle("");
#    w.setWindowIcon(QIcon('icon.png'))
#    app.exec_()