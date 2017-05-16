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
        return temp[0]

#if __name__ == '__main__':
#    jm = Jm()
#    jm.token = jm.login('yjx21644889','1111aaaa')
 #   jm.phone = jm.getMobilenum(jm.token,jm.username,'8445')

#    print jm.token,jm.phone



