#sendmail
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#sender='pingbao.liu@fisglobal.com'
#receivers=['pingbao.liu@fisglobal.com']#接收邮件

sender='form@runoob.com'
receivers=['lpb.waln@outlook.com']#接收邮件

#三个参数：第一个为文本内容，第二个plain设置文本格式，第三个utf-8设置编码
message=MIMEText('python发送邮件测试。。。','plain','utf-8')
message['From']=Header("菜鸟教程",'utf-8')
message['To']=Header("测试",'utf-8')

subject='python SMTP 邮件测试'
message['Subject']=Header(subject,'utf-8')

try:
    smtpObj=smtplib.SMTP('localhost')
    smtpObj.sendmail(sender,receivers,message.as_string())
    print('邮件发送成功')
except smtplib.SMTPException:
    print('Errot:无法发送邮件')
'''

import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
sender = 'runoob'
receivers = ['lpb.waln@outlook.com']  # 接收地址，可设置为你的QQ邮箱或者其他邮箱
 
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
#mail_msg='Python 邮件发送测试...'  #把邮件内容变量化
mail_msg="""
<p>Python 邮件发送测试...</p>
<p><a href="http://www.baidu.com">点击打开百度</a></p>
"""
message = MIMEText(mail_msg, 'html', 'utf-8')  #内容
message['From'] = Header("平宝python", 'utf-8')#发送者
message['To'] =  Header("接收测试", 'utf-8')#接收者
message['subject']=Header('Python SMTP 邮件测试','utf-8')#主题
#subject = 'Python SMTP 邮件测试'
#message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")
