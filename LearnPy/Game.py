class parent(object):
	def yinshi(self):
		print('隐士继承')
	def xianshi(self):
		print('显示替换')
	def super_all(self):
		print('super')
		
class child(object):
	def __init__(self):
		self.parent=parent()
	def xianshi(self):
		print('显示替换——替换')
	'''
	def super_all(self):
		print('super_down')
		super(child,self).super_all()
		print('super_down')
	'''
	def yinshijicheng(self):
		self.parent.yinshi()
		
p=parent()
c=child()

c.xianshi()
c.yinshijicheng()
#c.super_all()