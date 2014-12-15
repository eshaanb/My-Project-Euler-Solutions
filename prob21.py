def getFactorsSum(num):
	factors = []
	for i in range(1, num/2+1):
		if num % i == 0:
			factors.append(i)
	return sum(factors)

for i in range(1,10000):
	factorsSumList.append(getFactorsSum(i))

for index, factor in enumerate(factorsSumList):
	if factor < len(factorsSumList) and index == factorsSumList[factor] and index != factor and index not in addedList and factor not in addedList:
		print 'adding: ',index,factor
		addedList.append(index)
		addedList.append(factor)
		summ += index+factor