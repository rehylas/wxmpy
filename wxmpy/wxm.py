#encoding=utf-8

import os
import time
import requests
import json

URL = "http://www.bangnikanzhe.com/wx/sendstockmsg"
# URL = "http://127.0.0.1/wx/sendstockmsg"
userName=""
userPwd=""
 
def init(name, pwd):
    global userName
    global userPwd
    userName = name
    userPwd = pwd
    pass

def sendMsg(txt1,txt2,txt3):
    if userName == "":
        return '{"code": "9999","msg": "not init user name, call Init(name, pwd)"}'
    data = makeData(userName,userPwd,txt1,txt2,txt3)
    return postJson(data)


def sendMsgToUser(name,pwd,txt1,txt2,txt3):
    data = makeData(name,pwd,txt1,txt2,txt3)
    return postJson(data)

def postJson( data ):
    headers = {"Content-Type":"application/json"}
    try:
        jsdata = json.dumps( data )
        r=requests.post(URL,data=jsdata,headers=headers,timeout=3)
        # print r.text   
        return r.text    
    except Exception, e:
        print(e)
        return '{"code": "9999","msg": "http post error"}'
    pass

def makeData(name,pwd, txt1,txt2,txt3):
    msg = {"userid": name, "mark": "", "kw1": "kw1", "kw3": txt3, "kw2": txt2, "userpwd":  pwd,
        "first": txt1 }    
    return msg

# name = "80010120"
# pwd ="88888"
# txt1 ="a"
# txt2 ="b"
# txt3 ="c"
# result = sendMsgToUser(name, pwd,txt1,txt2,txt3)

# init(name, pwd)
# result = sendMsg(txt1,txt2,txt3)
# print(result) 

