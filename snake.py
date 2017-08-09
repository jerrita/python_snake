'''
bfs auto search path
created by wzq
version one
'''

import snwin
import snake_ai
import time
import os

win = snwin.snwin(15,15)
win.draw()

#print('蛇头：',win.snbody[0])

while True:
	win.go(snake_ai.bfsai(win.snbody[0],win.snmap,win.food,win.width,win.height))
	if win.lose == True:
		break
	win.clearmap()
	win.addmap()
	os.system('clear') 
	win.draw()
	time.sleep(0.05)

print('游戏结束！分数：',win.scor)
