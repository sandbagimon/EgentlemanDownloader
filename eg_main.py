# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 22:11:09 2019

@author: sandb
"""

import sys
from PyQt5.QtWidgets import QDialog, QApplication ,QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QIcon, QPixmap
from eg_uidialog import *
import requests
import bs4
import os
import re
import time
import threading
import login_dialog
import ast





class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.connect_button.clicked.connect(self.eh_connect)
        self.ui.download_button.clicked.connect(self.eh_download)
        self.ui.nextpage_button.clicked.connect(self.eh_next)
        self.ui.pervpage_button.clicked.connect(self.eh_pervious)
        
        self.checkboxs = [self.ui.doujinshi_cb,self.ui.manga_cb,self.ui.artist_cb,self.ui.game_cb,self.ui.western_cb,self.ui.nonh_cb,self.ui.image_cb,self.ui.cosplay_cb,self.ui.asia_cb,self.ui.misc_cb]
        for cbs in self.checkboxs:  
            cbs.stateChanged.connect(self.eh_update_parameters)
        
        self.ui.login_button.clicked.connect(self.eh_get_login)
        
        self.show()
        self.local_page = 0
        self.tags = {'f_doujinshi':'0','f_manga':'0','f_artistcg':'0','f_gamecg':'0','f_western':'0','f_non-h':'0','f_imageset':'0','f_cosplay':'0','f_asianporn':'0','f_misc':'0','f_apply':'Apply Filter','f_search' :'chinese mind control','f_apply':'Apply Filter','page':'0'}
        self.headers = {'User-Agent': 'Mozilla/5.0'}
    def eh_get_login(self):
        if os.path.exists('cookie.txt'):
            f=open('cookie.txt','r')
            a = f.read()
            a = re.findall('(\{[^\)]+\})', a)[0]
            self.cookie = ast.literal_eval(a)
            f.close()
            self.username = 'User'
            self.ui.textBrowser.append('Successfully logged in as ' + str(self.username) + '!')
            self.ui.connect_button.setEnabled(True)
            return
        w_login = login_dialog.LoginForm()
        if w_login.exec_():
            self.cookie,self.username = w_login.login()
            self.ui.textBrowser.append('Successfully logged in as ' + str(self.username) + '!')
            self.ui.connect_button.setEnabled(True)
        
    def eh_connect(self):
        with requests.Session() as self.client:
            requests.utils.add_dict_to_cookiejar(self.client.cookies,self.cookie)
            self.client.headers.update(self.headers)
            self.resp = self.client.post('https://exhentai.org',allow_redirects=False)    
            self.resp.encoding='urf-8'
            self.result=self.client.get('https://exhentai.org/?inline_set=dm_t') # 变成大图模式
        #    self.result=self.client.get('http://exhentai.org',params=self.tags)
            
            if self.result.status_code == 200:
                self.ui.textBrowser.append('Successfully connected !')
                self.ui.search_button.clicked.connect(self.eh_search)
                self.ui.search_button.setEnabled(True)
                self.ui.download_button.setEnabled(True)
                self.ui.search_button.setFocus()
                #连接成功
            else :
                self.ui.textBrowser.append('Something is wrong')
                #连接失败
            self.result.encoding='urf-8'
            
    def eh_search(self):
            self.local_page = 0
            self.tags['f_search']= self.ui.keywords_entry.text()
            self.tags['page'] = 0
            self.result = self.client.get('http://exhentai.org',params=self.tags)
            self.search_soup = bs4.BeautifulSoup(self.result.content,'lxml')
            self.eh_display_thumb(0)

    def eh_update_parameters(self):
        
        if self.ui.doujinshi_cb.isChecked()==True:
            self.tags['f_doujinshi']=1
        else :self.tags['f_doujinshi']=0
        
        if self.ui.manga_cb.isChecked()==True:
            self.tags['f_manga']=1
        else :self.tags['f_manga']=0
        
        if self.ui.artist_cb.isChecked()==True:
            self.tags['f_artistcg']=1
        else :self.tags['f_artistcg']=0
        
        if self.ui.game_cb.isChecked()==True:
            self.tags['f_gamecg']=1
        else :self.tags['f_gamecg']=0
        
        if self.ui.western_cb.isChecked()==True:
            self.tags['f_western']=1
        else :self.tags['f_western']=0
        
        if self.ui.nonh_cb.isChecked()==True:
            self.tags['f_non-h']=1
        else :self.tags['f_non-h']=0
        
        if self.ui.image_cb.isChecked()==True:
            self.tags['f_imageset']=1
        else :self.tags['f_imageset']=0
        
        if self.ui.cosplay_cb.isChecked()==True:
            self.tags['f_cosplay']=1
        else :self.tags['f_cosplay']=0
        
        if self.ui.asia_cb.isChecked()==True:
            self.tags['f_asianporn']=1
        else :self.tags['f_asianporn']=0
        
        if self.ui.misc_cb.isChecked()==True:
            self.tags['f_misc']=1
        else :self.tags['f_misc']=0
        return
    def eh_display_thumb(self,local_page):
        ## find all gallerys in current page and print
        count = int(self.tags['page'])*25

#        print('count = '+str(count))
#        print('global page = ' + str(self.tags['page']))

#        print('local page= ' + str(self.local_page))
        a = self.search_soup.find_all(attrs={'class':'id1'}) #大图模式
        for thumbs in a:
            count += 1            
            if count < local_page*5+1:
                continue
            if count > local_page*5+5:
                break ## 
#            print('count = '+str(count))
    #        ===================================
            self.scene = QGraphicsScene(self)
            pixmap= QtGui.QPixmap()
            pixmap.loadFromData(self.client.get(thumbs.img.get('src')).content)
            item=QGraphicsPixmapItem(pixmap)
            self.scene.addItem(item)
            if count == local_page*5+1:
                self.ui.graphicsView_1.setScene(self.scene) 
                self.ui.label_1.setText(thumbs.text)
            elif count == local_page*5+2:
                self.ui.graphicsView_2.setScene(self.scene)
                self.ui.label_2.setText(thumbs.text)
            elif count == local_page*5+3:
                self.ui.graphicsView_3.setScene(self.scene)
                self.ui.label_3.setText(thumbs.text)
            elif count == local_page*5+4:
                self.ui.graphicsView_4.setScene(self.scene)
                self.ui.label_4.setText(thumbs.text)
            elif count == local_page*5+5:
                self.ui.graphicsView_5.setScene(self.scene)
                self.ui.label_5.setText(thumbs.text)
 
#        ==================================
    def eh_next(self):
        self.local_page += 1

        if self.tags['page'] != (self.local_page)//5:
            self.tags['page'] = (self.local_page)//5
            self.result = self.client.get('http://exhentai.org',params=self.tags)
            self.search_soup = bs4.BeautifulSoup(self.result.content,'lxml')
        self.eh_display_thumb(self.local_page)
        return
    def eh_pervious(self):
        self.local_page -= 1
        if self.local_page <0:
            self.local_page = 0
        if self.tags['page'] != (self.local_page)//5:
            self.tags['page'] = (self.local_page)//5
            self.result = self.client.get('http://exhentai.org',params=self.tags)
            self.search_soup = bs4.BeautifulSoup(self.result.content,'lxml')
        self.eh_display_thumb(self.local_page)
#        ==================================
    def eh_download(self):
        local_page=  self.local_page
        count = int(self.tags['page'])*25
        for thumbs in self.search_soup.find_all(attrs={'class':'id1'}):
            count += 1
            if count < local_page *5:
                continue
            if count > local_page *5 + 5:
                break
                
            if (self.ui.checkBox_1.isChecked()==True and count==local_page*5+1):
                g_url = thumbs.a.get('href')
                g_title = re.sub('\||\/|\:|\*|\?|\<|\>|\/|\"',' ',thumbs.a.text)
                self.download(g_url,g_title)
                
            elif (self.ui.checkBox_2.isChecked()==True and count==local_page*5+2):
                g_url = thumbs.a.get('href')
                g_title = re.sub('\||\/|\:|\*|\?|\<|\>|\/|\"',' ',thumbs.a.text)
                self.download(g_url,g_title)
            elif (self.ui.checkBox_3.isChecked()==True and count==local_page*5+3):
                g_url = thumbs.a.get('href')
                g_title = re.sub('\||\/|\:|\*|\?|\<|\>|\/|\"',' ',thumbs.a.text)
                self.download(g_url,g_title)
            elif (self.ui.checkBox_4.isChecked()==True and count==local_page*5+4):
                g_url = thumbs.a.get('href')
                g_title = re.sub('\||\/|\:|\*|\?|\<|\>|\/|\"',' ',thumbs.a.text)
                self.download(g_url,g_title)
            elif (self.ui.checkBox_5.isChecked()==True and count==local_page*5+5):
                g_url = thumbs.a.get('href')
                g_title = re.sub('\||\/|\:|\*|\?|\<|\>|\/|\"',' ',thumbs.a.text)
                self.download(g_url,g_title)
            
            
    def download(self,url,title):
        #需要输入的是，gallery的url和gallery的title
        self.ui.textBrowser.append('Now Downloading. . .')
        start = time.time()# start
        count = 0
        if not os.path.exists(title):
            os.makedirs(title)
        page = self.client.get(url+'/?inline_set=ts_m')
        ## extact page HTML elements
        page_soup = bs4.BeautifulSoup(page.content,'lxml') 
        total_pages = int(page_soup.find('td',text=re.compile('pages')).text.split(' ')[0])  
        
        init_page_url = page_soup.find(attrs={'class':'gdtm'}).a.get('href') 
#        if init_page_url == None:
#            init_page_url = page_soup.find(attrs={'class':'gdtl'}).a.get('href') 
        
        init_page_elements = self.client.get(init_page_url)
        init_page_soup = bs4.BeautifulSoup(init_page_elements.content,'lxml')
        init_image_link =init_page_soup.find('img',id='img')['src']
        self.threads_start(init_image_link,count,title) # 开启多线程下载
        
        
        next_url = self.find_next_url(init_page_soup) 
        for i in range(total_pages-1):  
            count+=1
            image_soup = bs4.BeautifulSoup(self.client.get(next_url).content,'lxml') ## obtain the page elements of current image
            image_link = image_soup.find('img',id='img')['src'] ## find image address
            next_url = self.find_next_url(image_soup) ## update the next image url
            self.threads_start(image_link,count,title) # 开启多线程下载

#            start = time.time()
            #self.image_download(image_link,count,title)

#            end = time.time()
#            print('Total download time is '+str(end-start) +' seconds')
        self.ui.textBrowser.append('Download Completed !')
        end = time.time()
        print('Total download time is '+str(end-start) +' seconds')
    def find_next_url(self,soup):
        next_url = soup.find('div',id='i3').a['href']
        return next_url
    
    def threads_start(self,url,count,title):
        thread = threading.Thread(target = self.image_download,args=(url,count,title))
        thread.start()
        
    def image_download(self,url,count,title):

            
        file_name = (str(count))+('.jpg')     
        picture = self.client.get(url, stream=True)
        
        with open(str(title)+'/'+file_name,'wb') as f:
            for chunk in picture.iter_content(chunk_size=1024*1024):           
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
                    
if __name__=="__main__":
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    else: 
        print('QApplication instance already exists: %s' % str(app))

    w = MyForm()
    w.show
    w.setWindowTitle("Ex-君子/Ex-GentleMan");
    w.setWindowIcon(QIcon('icon.png'))
    app.exec_()