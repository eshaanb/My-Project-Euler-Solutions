def generateFib():
	last = 1
	start = 1
	for i in range(3,100000):
		tempLast = last
		last = start
		start = start+tempLast
		if len(str(start)) == 1000:
			print i
			return