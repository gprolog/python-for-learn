#sendmail

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  #附件相关
from email.mime.image import MIMEImage  #图片相关
from email.header import Header
 
sender = 'runoob'
receivers = ['lpb.waln@outlook.com']  # 接收地址，可设置为你的QQ邮箱或者其他邮箱
 
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
#mail_msg='Python 邮件发送测试...'  #把邮件内容变量化
mail_msg="""
<p>Python 邮件发送测试...</p>
<p><a href="http://www.baidu.com">点击打开百度</a></p>
<P>图片演示：</p>
<p><img src="cid:image1"></p>
"""

#创建带附件的邮件
msgRoot=MIMEMultipart('related')
#message = MIMEText(mail_msg, 'html', 'utf-8')  #内容
msgRoot['From'] = Header("平宝python", 'utf-8')#发送者
msgRoot['To'] =  Header("接收测试", 'utf-8')#接收者
msgRoot['subject']=Header('Python SMTP 带附件邮件测试','utf-8')#主题


#邮件正文内容
#message.attach(MIMEText(mail_msg,'html','utf-8'))


msgAlternative=MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgAlternative.attach(MIMEText(mail_msg,'html','utf-8'))

#指定图片为当前目录
fp=open('test.png','rb')
msgImage=MIMEImage(fp.read())
fp.close()

#定义图片ID，在HTML文本中引用
msgImage.add_header('Content-ID','<image1>')
msgRoot.attach(msgImage)
'''
#创建附件1,传递当前目录下的test.txt文件
att1=MIMEText(open('tiantian.txt','rb').read(),'base64','utf-8')
att1["Content-Type"]='application/octet-stream'
#这里的filename可以任意写，些什么名字，意味着邮件中显示什么
att1["Content-Disposition"]='attachment;filename="test.txt"'
message.attach(att1)
'''
try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, msgRoot.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")
