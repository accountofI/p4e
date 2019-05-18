myList = []
fhand = open('romeo.txt')
for line in fhand:
	words = line.split()				#Splits line into array of words
	for word in words:
		if word in myList : continue	#Discards duplicates
		myList.append(word)				#Updates the list
print(sorted(myList))					#Alphabetical orderprint(lst)