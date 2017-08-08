import os
import random

class snwin:
	def __init__(self,wid,hei):
		self.width = wid
		self.height = hei
		self.snmap = []
		self.sndire = '6'
		self.snbody = [(2,2),(3,2)]
		self.snhead = (3,2)
		self.sntail = (2,2)
		self.snshow = '*'
		
		#地图初始化
		for i in range(0,hei):
			self.snmap.append([])
			for j in range(0,wid):
				self.snmap[i].append(' ')
				if i == 0 or i == hei - 1 or j == 0 or j == wid - 1:
					self.snmap[i][j] = '#'
					
		self.spanfood()
					

	def draw(self):
		os.system('clear')
		self.addsnake()
		for i in self.snmap:
			for j in i:
				print(j,end=' ')
			print('')
			
	def mpadd(self,x,y,z):
		self.snmap[y][x] = z
	def mpdel(self,x,y):
		self.snmap[y][x] = ' '
	def addsnake(self):
		for i in self.snbody:
			self.mpadd(i[0],i[1],self.snshow)
	def spanfood(self):
		x = random.randint(1,self.width - 1)
		y = random.randint(1,self.height - 1)
		if (x,y) in self.snbody:
			self.sneat()
		else:
			self.food = (x,y)
			self.mpadd(x,y,'@')
