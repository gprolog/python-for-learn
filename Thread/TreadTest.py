# import thread 
# import time
# import threading

# def Print_time(name,delay):
	# count=0
	# while count<5:
		# count+=1
		# time.sleep(delay)
		# print('%s,%s'%(name,time.ctime(time.time())))
# try:
	# thread.start_new_thread(Print_time,('thread-1',2))
	# thread.start_new_thread(Print_time,('thread-2',4))
	# print('thread-2 start')
# except:
	# print('Erro')
# while 1:
	# pass
	
import threading
import time
exitflag=0

class my_thread(threading.Thread):
	def __init__(self,threadid,name,counter):
		threading.Thread.__init__(self)
		self.threadid=threadid
		self.name=name
		self.counter=counter
	def run(self):
		#currentname=threading.currentThread()
		#print('running in %s' %currentname)
		print('starting',self.name)
		show_time(self.name,3,6)
		print('Exiting',self.name)

def show_time(name,delay,counter):
	while counter:
		if exitflag:
			threading.Thread.exit()
		time.sleep(delay)
		print('%s,%s'%(name,time.ctime(time.time())))
		counter-=1
	
thread1=my_thread(1,'thread1',5)
thread2=my_thread(2,'thread2',5)
thread1.start()
thread2.start()