# -*- coding: utf-8 -*-
import requests
import json
from jm import Jm
from cookie import change_cookie
jm = Jm()


print jm.phone
token =  jm.login('yjx21644889','1111aaaa')
print token
phone = jm.getMobilenum(token,jm.username,"8445")
print phone



params = dict(mobile=phone,username='',password='',captcha='voiog',key='')
cookie = 'PHPSESSID=3rfukb7b9d1kqss7mk5odichr4; UM_distinctid=15c2fcd31450-0abc351e634038-51462d15-1fa400-15c2fcd3146329; city=110000; cityname=%E5%8C%97%E4%BA%AC%E5%B8%82; area_id=110101; storeid=485; storename=%E4%B8%9C%E5%9B%9B%E5%8D%97%E5%A4%A7%E8%A1%97%EF%BC%88%E5%A6%82%E6%84%8F%E9%A6%84%E9%A5%A8%EF%BC%89; address=东城区东四南大街灯草胡同66号如意馄饨; iweb_safecode=bc904c4d9bMTU5NTMzMDUyMmYwNWFhMzYyMjxmMjU6MDg6MmVlMTc; iweb_shoppingcart=637566683dMDc2MDcyNTA2MGQyMWZiOGU1PzE0YmRqODkxNzs2YDt7JmNraW1zIDhbXCUvcHptZ3VkdCE4W119; session_id=3rfukb7b9d1kqss7mk5odichr4; CNZZDATA1254019111=754524366-1495448181-%7C1495535085'
r = requests.post('http://www.xuxian.com/index.php?controller=simple&action=getCode',data=params,cookies=change_cookie(cookie))
print r.text

#code = r.t
