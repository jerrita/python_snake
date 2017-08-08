import snwin

win = snwin.snwin(20,20)
win.draw()

while True:
	di = input('')
	if di == '2' or di == '4' or di == '5' or di == '6':
		win.go(di)
		win.draw()
