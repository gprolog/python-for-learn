#创建server
import socket
import sys
#创建socket对象
serverscoket=socket.socket (socket.AF_INET ,socket.SOCK_STREAM )

#获取本地主机名称
host=socket.gethostname ()
port=9090

#绑定IP和端口
serverscoket.bind((host,port))

#设置最大连接数，超过后排队
serverscoket.listen(5)

while True:
    #建立客户端连接
    clientsocket,addr=serverscoket.accept()
    print('连接地址：%s' % str(addr))

    msg='欢迎访问菜鸟教程！'+'\r\n'
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()
