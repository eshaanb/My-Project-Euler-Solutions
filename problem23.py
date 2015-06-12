
#construct a list of abundant numbers under 28k
for i in xrange(1,28123):
	if getDivisorSum(i) > i:
		#is abundant
		abundantNumbers.append(i)

a = range(0,28123)

#order of n^2 runtime because we add the abundant numbers to each other and remove them from master list
for idx, abundantNum in enumerate(abundantNumbers):
	for num2 in abundantNumbers[idx:]:
		checkNum = abundantNum+num2
		maxNum = a[len(a)-1]
		if checkNum > maxNum:
			break
		else:
			try:
				index = a.index(checkNum)
				del a[index]
			except ValueError:
				pass
	print "finished: "+str(abundantNum)