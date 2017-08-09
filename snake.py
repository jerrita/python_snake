import snwin
import snake_ai
import time
import os

win = snwin.snwin(15,15)
win.draw()

while True:
	win.go(snake_ai.ai(win.snbody,win.food))
	if win.lose == True:
		break
	win.clearmap()
	win.addmap()
	os.system('clear')
	win.draw()
	time.sleep(0.1)

print('游戏结束！分数：',win.scor)