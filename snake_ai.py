def ai(body,food):
	a = body[0]
	b = food
	if a[1] < b[1]:
		return 5
	if a[1] > b[1]:
		return 2
	if a[1] == b[1]:
		if a[0] < b[0]:
			return 6
		if a[0] > b[0]:
			return 4