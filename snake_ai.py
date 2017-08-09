'''
bfs auto search path
created by wzq
version one
'''

def bfsai(head,snmap,food,wid,hei):
	status = [([False] * hei) for i in range(wid)]
	v = []
	v.append(food)
	step = 1
	searched = []
	while len(v) != 0:
		step += 1
		search = v.pop()
		if search in searched: continue
		else: searched.append(search)
		mapblock = snmap[search[0]][search[1]] 
		if search == head: break
		if mapblock == '*': continue
		if mapblock == '#': continue
		if snmap[search[0]+1][search[1]] == ' ':
			status[search[0]+1][search[1]] = step
			v.insert(0,(search[0]+1,search[1]))
		if snmap[search[0]-1][search[1]] == ' ':
			status[search[0]-1][search[1]] = step
			v.insert(0,(search[0]-1,search[1]))
		if snmap[search[0]][search[1]+1] == ' ':
			status[search[0]][search[1]+1] = step
			v.insert(0,(search[0],search[1]+1))
		if snmap[search[0]][search[1]-1] == ' ':
			status[search[0]][search[1]-1] = step
			v.insert(0,(search[0],search[1]-1))
	status[food[0]][food[1]] = 1
	go = {
	 2:status[head[0]][head[1]-1],
	 5:status[head[0]][head[1]+1],
	 4:status[head[0]-1][head[1]],
	 6:status[head[0]+1][head[1]]
	}
	if go[2] == False: del go[2]
	if go[4] == False: del go[4]
	if go[6] == False: del go[6]
	if go[5] == False: del go[5]
	method = sorted(go.items(), key=lambda d:d[1], reverse = True)
	if len(method) != 0: return method.pop()[0]
	print('Kdf ai cannot find the path!')
	exit()