'''
bfs auto search path
created by wzq
version two
'''

import random

class snwin:
	def __init__(self,width,height):
		self.width = width
		self.height = height
		self.snbody = [(3,2),(2,2)]
		self.lose = False
		self.scor = 0
		self.di = 6
		self.frame = '#'
		self.snblock = 'O'
		self.foodblock = '@'
		self.snmap = []
		self.clearmap()
		self.spanfood()
		self.addmap()
	
	#绘图
	def draw(self):
		print('Scor:',self.scor)
		'''
		for y in range(self.height):
			for x in range(self.width):
				print(self.snmap[x][y],end=' ')
			print('')
		'''
		for i in self.snmap:
			print(' '.join(i))
		print('')
		
	#移动
	def go(self,di = 0):
		if di not in [2,5,4,6]:
			di = self.di
		else:
			self.di = di
		
		if di == 2:
			self.snbody.insert(0,(self.snbody[0][0],self.snbody[0][1]-1))
		if di == 5:
			self.snbody.insert(0,(self.snbody[0][0],self.snbody[0][1]+1))
		if di == 4:
			self.snbody.insert(0,(self.snbody[0][0]-1,self.snbody[0][1]))
		if di == 6:
			self.snbody.insert(0,(self.snbody[0][0]+1,self.snbody[0][1]))
		
		#碰撞检测
		old_block = self.snmap[self.snbody[0][0]][self.snbody[0][1]]
		if old_block == self.frame:
			self.lose = True
		if old_block == self.snblock:
			self.lose = True
		if old_block == self.foodblock:
			self.scor += 1
			self.spanfood()
		else:
			del self.snbody[-1]
		
	#食物生成
		
	def spanfood(self):
		x = random.randint(1,self.width - 2)
		y = random.randint(1,self.height - 2)
		if (x,y) in self.snbody:
			self.spanfood()
		else:
			self.food = (x,y)
	
	#地图添加
	
	def addmap(self):
		self.addfood()
		self.addsnake()
		
	def clearmap(self):
		self.snmap = [([' '] * self.height) for i in range(self.width)]
		for i in range(self.width):
			for j in range(self.height):
				if i == 0 or i == self.width-1 or j == 0 or j == self.height-1:
					self.snmap[i][j] = self.frame
		
		
	def addfood(self):
		self.snmap[self.food[0]][self.food[1]] = self.foodblock
		
	def addsnake(self):
		for i in self.snbody:
			self.snmap[i[0]][i[1]] = self.snblock