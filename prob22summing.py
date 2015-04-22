f = open('/users/eshaan/desktop/sorted.txt', 'r')
sortedNames = f.readlines()
f.close()
nameDict = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 'j' : 10, 'k' : 11, 'l' : 12, 'm' : 13, 'n' : 14, 'o' : 15, 'p' : 16, 'q' : 17, 'r' : 18, 's' : 19, 't' : 20, 'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24, 'y' : 25, 'z' : 26}

summed = 0
for idx, name in enumerate(sortedNames):
	nameSummed = 0
	name = name.rstrip()
	for character in list(name):
		nameSummed += nameDict[character.lower()]
	summed += nameSummed*(1+idx)

print(str(summed))