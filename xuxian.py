# -*- coding: utf-8 -*-
import requests
import time
import json
from jm import Jm
from cookie import change_cookie
jm = Jm()


print jm.phone
token =  jm.login('yjx21644889','888888888')
print token
phone = jm.getMobilenum(token,jm.username,"8445")
print phone



params = dict(mobile=phone,username='',password='',captcha='ajeta',key='')
cookie = 'UM_distinctid=15c2fcd31450-0abc351e634038-51462d15-1fa400-15c2fcd3146329; city=110000; cityname=%E5%8C%97%E4%BA%AC%E5%B8%82; area_id=110101; storeid=485; storename=%E4%B8%9C%E5%9B%9B%E5%8D%97%E5%A4%A7%E8%A1%97%EF%BC%88%E5%A6%82%E6%84%8F%E9%A6%84%E9%A5%A8%EF%BC%89; address=东城区东四南大街灯草胡同66号如意馄饨; PHPSESSID=o5vn49b0vmogm7gdb226uf4sq2; iweb_safecode=b82cf292f8MTAwMDk4MDc4N2E2N2FhNj4yNT1gMjA6NDsxMWRmMTI; iweb_shoppingcart=0c1066ae96MjYwNDIwMjQ2MWQwM2tiNGQ5MDE0Y2NiODk1Njk0ZTh7I2dqbGJzLzNdVCMlcHpuZXxkdyY6W111; CNZZDATA1254019111=754524366-1495448181-%7C1495622035; session_id=o5vn49b0vmogm7gdb226uf4sq2'
r = requests.post('http://www.xuxian.com/index.php?controller=simple&action=getCode',data=params,cookies=change_cookie(cookie))

temp = json.loads(r.text)
print temp

if (temp["code"] == True):
    message='not_receive'
    while (message=='not_receive'):
        message =jm.getVcodeAndReleaseMobile(jm.username,token,phone)
        print message
        time.sleep(10)
