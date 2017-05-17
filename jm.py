import requests

class Jm:
    url = 'http://api.jmyzm.com/http.do'
    token = ''
    username=''
    phone = ''
    def login(self,username, password):
        self.username=username
        params = dict(action='loginIn',uid=username,pwd=password)
        r = requests.post(self.url,params)
        temp= r.text.split('|')
        return temp[1]

    def getMobilenum(self,token,username,pid):

        params = dict(action='getMobilenum',pid=pid ,uid= username ,token= token)
        r = requests.post(self.url,params)
        temp= r.text.split('|')
        self.phone=temp[0]
        return temp[0]

    def getVcodeAndReleaseMobile(self,username,token,phone):
        params = dict(action='getVcodeAndReleaseMobile',uid= username ,token= token,mobile=phone,author_uid='yjx21644889')
        r = requests.post(self.url,params)
        return r.text

    def addIgnoreList(self,username,token,phone,pid):
        params = dict(action='addIgnoreList',uid= username ,token= token,mobile=phone,pid=pid)
        r = requests.post(self.url,params)
        return r.text

