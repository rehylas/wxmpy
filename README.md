# wxmpy: wx message for python
发送微信信息到自己手机

# install
pip install wxmpy

#   github
github.com/rehylas/wxmpy

#   usage

    ``` 
        import wxmpy

        print(wxmpy)
        name = "80010120"  # 改成自己的  username  和 userpwd
        pwd ="88888"
        txt1 ="a"
        txt2 ="b"
        txt3 ="c"
        result = wxmpy.sendMsgToUser(name, pwd,txt1,txt2,txt3)

        wxmpy.init(name, pwd)
        result = wxmpy.sendMsg(txt1,txt2,txt3)
        print(result) 

    ```    

效果
![Image text](http://www.bangnikanzhe.com/img/wxm.jpg)

#  如何获得 name 和 pwd  , 扫码并关注, 会自动获得 name 和 pwd：
![Image text](http://www.bangnikanzhe.com/img/bnkz10003.jpg)




