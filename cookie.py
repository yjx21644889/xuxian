
def change_cookie(text):
    cookie = {}
    temp=text.split(';')
    for x in temp:
        temp1 = x.split('=')
        cookie[temp1[0]]=temp1[1]
    return cookie
