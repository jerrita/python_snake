import os
import random

class snwin:
	def __init__(self,wid,hei):
		self.width = wid
		self.height = hei
		self.snmap = []
		self.snbody = [(3,2),(2,2)]
		self.snhead = (3,2)
		self.sndire = '6'
		self.border = '■'
		self.snshow = '●'
		self.snhdsh = '◆'
		self.snfood = '※'
		self.lose = False
		self.scor = 0
		
		#地图初始化
		for i in range(0,hei):
			self.snmap.append([])
			for j in range(0,wid):
				self.snmap[i].append(' ')
				if i == 0 or i == hei - 1 or j == 0 or j == wid - 1:
					self.snmap[i][j] = self.border
					
		self.spanfood()
		
	def clearmap(self):
		for i in range(0,self.height):
			for j in range(0,self.width):
				if self.snmap[i][j] != self.border:
					self.snmap[i][j] = ' '

	def draw(self):
		os.system('clear')
		self.addfood()
		self.addsnake()
		print('Scor:',self.scor)
		for i in self.snmap:
			for j in i:
				print(j,end=' ')
			print('')
			
	def go(self,di=''):
		if di not in ['6','5','4','2']:
			di = self.sndire
		if di == '6':
			self.sndire = '6'
			self.snbody.insert(0,(self.snhead[0]+1,self.snhead[1]))
			self.snhead = self.snbody[0]
		elif di == '5':
			self.sndire = '5'
			self.snbody.insert(0,(self.snhead[0],self.snhead[1]+1))
			self.snhead = self.snbody[0]
		elif di == '4':
			self.sndire = '4'
			self.snbody.insert(0,(self.snhead[0]-1,self.snhead[1]))
			self.snhead = self.snbody[0]
		elif di == '2':
			self.sndire = '2'
			self.snbody.insert(0,(self.snhead[0],self.snhead[1]-1))
			self.snhead = self.snbody[0]
		#走完一步后进行碰撞检测与食物判断
		hdblock = self.gtfmap(self.snhead[0],self.snhead[1])
		if hdblock == self.border:
			#game over
			self.lose = True
		if (self.snhead[0],self.snhead[1]) in self.snbody[1:]:
			self.lose = True
		if hdblock == self.snfood:
			#eat food
			self.scor += 1
			self.spanfood()
		else:
			del self.snbody[-1]
	def mpadd(self,x,y,z):
		self.snmap[y][x] = z
	def gtfmap(self,x,y):
		return self.snmap[y][x]
	def addsnake(self):
		for i in self.snbody:
			self.mpadd(i[0],i[1],self.snshow)
		self.mpadd(self.snhead[0],self.snhead[1],self.snhdsh)
	def spanfood(self):
		x = random.randint(1,self.width - 3)
		y = random.randint(1,self.height - 3)
		if (x,y) in self.snbody:
			self.spanfood()
		else:
			self.food = (x,y)
	def addfood(self):
		self.mpadd(self.food[0],self.food[1],self.snfood)
