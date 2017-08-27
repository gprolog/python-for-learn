#0002，将生成的激活码保存到oracle数据库中

import string
import random
import cx_Oracle


forselect=string.ascii_letters +string.digits

def codes(count,length):  #生成激活码
     for x in range(count):
         Re=''
         for y in range(length):
             Re+=random.choice (forselect)
         yield Re   #yield生成器，有返回值
         print(Re)
     print('激活码数量为：',count)
     
def insertcode():   #连接数据库
    database_user = 'core'
    database_pwd = 'core'
    database_ip = '127.0.0.1'
    database_port = 1521
    database_service = 'xe'
    database_url = '{}/{}@{}:{}/{}'.format(database_user, database_pwd, database_ip, database_port, database_service)

    conn=cx_Oracle.connect(database_url)  #建立连接
    cursor=conn.cursor()   #我们要使用连接对象获得一个cursor对象,接下来,我们会使用cursor提供的方法来进行工作，1.执行命令，2.接受返回值
    print('cursor',cursor)
    onecode=codes(10,20)  #调用激活码生成方法
    for mycode in onecode:       
        cursor.execute ("insert into code (code) values('%s')"%mycode)  #插入数据库，注意string类型变量的处理
        conn.commit()  #提交
        print('数据库插入成功')
    cursor.close() #关闭cursor
    conn.close()  #关闭连接
       
if __name__ =='__main__':
    insertcode()
