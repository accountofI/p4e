# Use words.txt as the file name
file=input("ENTER FILE : ")
fhand = open(file)
counts = dict()
t = list()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in t:
            t.append(word)
t.sort()
print(t)