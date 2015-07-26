# -*- coding:utf8 -*-
import json
from lxml import etree
import requests

__author__ = 'arthur'
email='******'
psw = '*****'

def autosign_ne2x():
    header_info = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1581.2 Safari/537.36',
        'Host': 'ne2x.com',
        'Origin': 'http://ne2x.com/',
        'Connection': 'keep-alive',
        'Referer': 'http://ne2x.com/auth/login',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    s = requests.session()
    #r = s.get('http://ne2x.com/', headers=header_info)
    r = s.get('http://ne2x.com/auth/login', headers=header_info)

    content = r._content
    cookies = r.cookies

    #lxml xpath获取token
    page= etree.HTML(content)
    x = page.xpath("//html//body//div[1]//div//div//form//div[1]//input")
    token = x[0].get('value')
    print token

    data ={'_token': token, 'button': '', 'email': email, 'password': psw}
    s.headers = header_info
    r = s.post('http://ne2x.com/auth/login', data=data)
    r = s.get('http://ne2x.com/', headers=header_info)

    #更改referer 加上X-CSRF-TOKEN
    header_info['Referer'] = 'http://ne2x.com/'
    header_info['X-CSRF-TOKEN'] = token
    s.headers = header_info
    r = s.post('http://ne2x.com/daily_mission')


    print 'ne2x sign '+ r._content

autosign_ne2x()