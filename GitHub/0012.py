'''
第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，
例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

北京
程序员
公务员
领导
牛比
牛逼
你娘
你妈
love
sex
jiangge
'''

word_filter=set()
filepath='C:\\WorkDay\\Code\\Python\\MyPython\\GitHub\\src\\filtered_words.txt'

with open(filepath) as f:
    words=f.readlines()
    for w in words:
        word_filter.add(w.strip())

while True:
    s=input('请输入\n')

    if s=='exit':
        break
    for w in word_filter:
        if w in s:
            s=s.replace(w,'*'*len(w))
            print(s)
