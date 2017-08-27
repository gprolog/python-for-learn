#thread

import _thread
import time

#为线程定义一个函数
def print_time(threadname,delay):
    count=0
    time.sleep(delay)
    while count<5:
        count+=1
        print('%s:%s' % (threadname,time.ctime(time.time())))

#创建两个线程
try:
    _thread.start_new_thread(print_time,('thread1',1))
    _thread.start_new_thread(print_time,('thread2',2))

except:
    print('Error：线程无法启动')
