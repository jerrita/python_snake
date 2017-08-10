'''
bfs auto search path
created by wzq
version one
'''
import random

def bfsai(win):
	method = bfs(win,win.food)
	if len(method) == 0:
		method = bfs(win,win.snbody[-1])
		if len(method) == 0:
			method = wander(win.snbody[0],win.snmap)
			if method == False: exit()
			else: return method
		else:
			return method[0][0]
	else:
		return method[-1][0]
	
def bfs(win,goal):
	status = [([False] * win.height) for i in range(win.width)]
	v = []
	v.append(goal)
	step = 1
	searched = []
	while len(v) != 0:
		step += 1
		search = v.pop()
		if search in searched: continue
		else: searched.append(search)
		mapblock = win.snmap[search[0]][search[1]] 
		if search == win.snbody[0]: break
		if search != goal:
			if mapblock == win.snblock: continue
		if mapblock == win.frame: continue
		if win.snmap[search[0]+1][search[1]] == ' ':
			status[search[0]+1][search[1]] = step
			v.insert(0,(search[0]+1,search[1]))
		if win.snmap[search[0]-1][search[1]] == ' ':
			status[search[0]-1][search[1]] = step
			v.insert(0,(search[0]-1,search[1]))
		if win.snmap[search[0]][search[1]+1] == ' ':
			status[search[0]][search[1]+1] = step
			v.insert(0,(search[0],search[1]+1))
		if win.snmap[search[0]][search[1]-1] == ' ':
			status[search[0]][search[1]-1] = step
			v.insert(0,(search[0],search[1]-1))
	status[goal[0]][goal[1]] = 1
	go = {
	 2:status[win.snbody[0][0]][win.snbody[0][1]-1],
	 5:status[win.snbody[0][0]][win.snbody[0][1]+1],
	 4:status[win.snbody[0][0]-1][win.snbody[0][1]],
	 6:status[win.snbody[0][0]+1][win.snbody[0][1]]
	}
	if go[2] == False: del go[2]
	if go[4] == False: del go[4]
	if go[6] == False: del go[6]
	if go[5] == False: del go[5]
	method = sorted(go.items(), key=lambda d:d[1], reverse = True)
	return method
			
def wander(head,snmap):
	method = []
	if snmap[head[0]+1][head[1]] == ' ': method.append(6)
	if snmap[head[0]-1][head[1]] == ' ': method.append(4)
	if snmap[head[0]][head[1]+1] == ' ': method.append(5)
	if snmap[head[0]][head[1]-1] == ' ': method.append(2)
	if len(method) == 0: return False
	else: return random.choice(method)