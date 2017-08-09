import snwin
import time
import os

win = snwin.snwin(15,15)
win.draw()

def ai(a,b):
	if a[1] < b[1]:
		return '5'
	if a[1] > b[1]:
		return '2'
	if a[1] == b[1]:
		if a[0] < b[0]:
			return '6'
		if a[0] > b[0]:
			return '4'

while True:
	next = ai(win.snhead,win.food)
	win.go(next)
	if win.lose == True:
		break
	win.clearmap()
	win.draw()
	time.sleep(0.05)

os.system('clear')
print('游戏结束！得分:',win.scor)

