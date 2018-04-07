'''
import re
line="Cats are smater than dogs"
matchObj=re.match('(.*)are(.*?).*',line)
print(matchObj.group())
'''
'''
import re
line='Cat are smarter than dogs'
matchObj=re.match(r'are',line,re.M|re.I)
if matchObj:
    print('re.match匹配结果:',matchObj.group())
else:
    print('No Match')

 
searchObj=re.search(r'dogs',line,re.M|re.I)
if searchObj:
    print('re.search匹配结果：',searchObj.group())
else:
    print('No Match')

'''

import re
phone='185-162-92278 #这是一个电话号码'
print(phone)
num=re.sub(r'#.*$','',phone)
print('去掉非数字后的号码：',num)

num2=re.sub(r'\D','',phone)
print('去掉分隔符后的号码:',num2)
