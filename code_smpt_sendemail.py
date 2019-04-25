# !/usr/bin/env python
# -*-coding:utf-8-*-
# coder:sjh
# version:1.0
"""
演示：通过SMTP协议发送邮件，  
使用163 邮箱作为测试：
用户名
密码
第三方授权码
"""
import smtplib
import email
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import os
# FROM_ADDR=os.environ.get("FROM_ADDR")
# FROM_PSWD=os.environ.get("FROM_PSWD")
# print FROM_ADDR, FROM_PSWD
"""win 环境下：先set FROM_ADDR = "test@163.com" FROM_PSWD = "123456"
linix环境下：用export """

"""          os.environ.get('path')
             os.environ.get('USERNAME')
              先设置变量（环境变量）
              cmd 
             import os
             set FROM_PSWD=123456
             print os.environ.get("FROM_PSWD")
             export  设置 linix环境命令
             set  设置 Windows环境命令     ----命令行set 是一次性的
             把敏感信息都写到本地计算机环境变量中，再使用environ调用,可以实现永久性   ----永久性的
"""

from_str = "Python爱好者 <test@163.com>"
to_str = "丽丽 <test@163.com>"
print parseaddr(from_str)
name, addr = parseaddr(from_str)
print name, addr

name, addr = parseaddr(to_str)
print name, addr

print Header(u"I am lucy","utf-8").encode()
print Header(u"来自XX的问候","utf-8").encode()
#返回的值是个tuple？
#类里面提到  是一个私有函数，可以用，但是不提倡用

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name,"utf-8").encode(),addr))

print _format_addr(from_str)
print _format_addr(to_str)

def send_email():
    from_addr = u"test@163.com"
    password = u"123456"   #163设置的第三方授权密码
    # from_addr=FROM_ADDR
    #password=FROM_PSWD

    to_addr = u"test@163.com"
    smtp_server=u"smtp.163.com"
    # smtp_server=u"smtp.qq.com"
    # smtp_server=u"smtp.126.com"

    msg=MIMEText(u"hello,send by automation","plain","utf-8")
    msg['From']=_format_addr(u"Python爱好者<%s>"%from_addr)
    msg["To"]=_format_addr(u"管理员<%s>"%to_addr)
    msg["Subject"]=Header(u"来自SMTP的问候……","utf-8").encode()

    server=smtplib.SMTP(smtp_server)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr],msg.as_string())
    server.quit()
    print"send ok"

if __name__ == "__main__":
    send_email()
    # pass

""" ------------------------------------
  设置的第三方授权:作用：隐藏敏感信息,比如 账号 密码
  --------------------------------------"""