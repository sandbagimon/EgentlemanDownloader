# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 16:31:19 2019

@author: sandb
"""

import requests





def get_dict_cookies(username,password):
    userpass = {'UserName':'','PassWord':'','ipb_login_submit':'Login!','CookieDate':'1'}
    headers = {'User-Agent': 'Mozilla/5.0','connection': 'keep-alive'}
    with requests.Session() as client:
        userpass['UserName'] = username
        userpass['PassWord'] = password
        client.headers.update(headers)
        a = client.post('https://forums.e-hentai.org/index.php?act=Login&CODE=01',data = userpass)
        a.encoding='urf-8'
        cookie = a.cookies.get_dict()
        return cookie

