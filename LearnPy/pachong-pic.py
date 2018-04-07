import os
import requests
from bs4 import BeautifulSoup

url='http://tieba.baidu.com/p/4412231996'
html=requests.get(url)
soup=BeautifulSoup(html.text,'html.parser')
img_urls=soup.findAll('img',class_='BDE_Image')
save_path='C:/download/'  #定义保存目录
html.close()

for img_url in img_urls:
    img_src=img_url['src']
    os.path.split(img_src)[1]
    print(os.path.split(img_src)[1])
    
    with open(save_path+os.path.split(img_src)[1],'wb') as f:
        f.write(requests.get(img_src).content)
        f.close()
        
