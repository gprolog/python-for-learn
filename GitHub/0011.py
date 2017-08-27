'''
#第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
#当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

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

#encoding=gbk

word_filter=set()
filepath='C:\\WorkDay\\Code\\Python\\MyPython\\GitHub\\src\\filtered_words.txt'
with open(filepath) as f:
    for w in f.readlines():
        word_filter.add(w.strip())  #Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）。
        print (w)


while True:
    s=input('请输入检查的词汇，输入exit退出\n')
    if s=='exit':
        break
    if s in word_filter:
        print('Freedom')
    else:
        print('Human Rights')

