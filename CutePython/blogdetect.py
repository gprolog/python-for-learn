#输入博客地址，监测blog的编码格式

import sys
import urllib.request  #在3.x版本中没有urllib2库，是urllib
import chardet

def blog_detect(blogurl):

    try:
        fp =urllib.request.urlopen(blogurl)
        
    except Exception:
        #print e
        print ('download exception %s'% blogurl)
        return 0
    blog=fp.read()
    codedetect=chardet.detect(blog)['encoding']
    print('%s\t<-\t%s' % (blogurl,codedetect))
    fp.close()
    return 1
if __name__=='__main__':
    blog_detect('http://www.imooc.com/')
