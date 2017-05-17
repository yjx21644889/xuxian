
from jm import Jm
jm = Jm()

print jm.phone
token =  jm.login('yjx21644889','1111aaaa')
print token
phone = jm.getMobilenum(token,jm.username,"8445")
print phone
temp = jm.getVcodeAndReleaseMobile(jm.username,token,phone)
print temp
temp = jm.addIgnoreList(jm.username,token,phone,'8445')
print temp
print jm.phone