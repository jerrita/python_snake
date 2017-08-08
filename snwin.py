import os

class snwin:
	def __init__(self,wid,hei):
		self.width = wid
		self.height = hei
		self.snmap = []
		
		#地图初始化
		for i in range(0,hei):
			self.snmap.append([])
			for j in range(0,wid):
				self.snmap[i].append('  ')
				if i == 0 or i == hei - 1 or j == 0 or j == wid - 1:
					self.snmap[i][j] = '# '

	def draw(self):
		os.system('clear')
		for i in self.snmap:
			for j in i:
				print(j,end='')
			print('')
