def dosim():
	current = [0,1,2,3,4,5,6,7,8,9]
	loopPermutate(current, 1)

def loopPermutate(starting, count):
	while count < 1000000:
		next = permutate(starting)
		count += 1
	print str(next)

def permutate(current):
	for idx, num in reversed(list(enumerate(current))):
		if idx == 0:
			print "finished"
			return current
		realnum = current[idx-1]
		realidx = idx-1
		if realnum < num:
			for idx2, num2 in reversed(list(enumerate(current))):
				if num2 > realnum:
					current[realidx] = num2
					current[idx2] = realnum
					current[idx:] = reversed(current[idx:])
					return current