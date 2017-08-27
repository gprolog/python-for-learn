#第 0006 题： 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，
#请统计出你认为每篇日记最重要的词。
import os
import re

Dirpath='C:\\download\\file\\'

def findWord(Dirpath):
    if not os.path.isdir(Dirpath):
        return
    filelist=os.listdir(Dirpath)
    reObj=re.compile('\b?(\w+)\b?')  #匹配单词的正则表达式
    for file in filelist:
        filepath=os.path.join(Dirpath,file)  #将文件名和路径拼接
        #print('filepath=',filepath)
        if os.path.isfile(filepath)and os.path.splitext(filepath)[1]=='.txt':  #splittext()分割路径，返回路径名和文件扩展名的元组
            with open (filepath)as f:
                data=f.read()
                words=reObj.findall(data)
                wordDict=dict()
                for word in words:
                    word=word.lower() #将大写转换为小写
                   # print('word=',word)
                    if word in ['a','the','to']:
                        continue
                    if word in wordDict:
                        wordDict[word]+=1
                    else:
                        wordDict[word]=1
            ansList=sorted(wordDict.items(),key=lambda t:t[1],reverse=True)  #sorted()产生一个新的列表
            print('file:%s->the most word:%s' % (file,ansList[1]))

if __name__=='__main__':
    findWord(Dirpath)
