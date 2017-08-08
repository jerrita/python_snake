import snwin
import time
import os

win = snwin.snwin(15,15)
win.draw()

while True:
	win.go(input(''))
	if win.lose == True:
		break
	win.clearmap()
	win.draw()
	time.sleep(0.5)

os.system('clear')
print('游戏结束！得分:',win.scor)
