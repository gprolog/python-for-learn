#004任一个英文的纯文本文件，统计其中的单词出现的个数。
import re
from collections import Counter

def word_count(txt):
    word_pattern=r'[a-zA-Z-]+'
    words=re.findall (word_pattern,txt)
    return Counter(words).items()

if __name__=='__main__':
    txt=open('testword.txt','r').read().lower()
    print (word_count(txt))
