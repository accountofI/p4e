7.2
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open("mbox-short.txt")
a = []
m=0
c=0
count=float(c)
s=float(m)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else:
        ipos = line.find(':')
        piece = line[ipos+2:]
        value=  float(piece)
        s=s+value
        count=count+1
average=s/count
print("Average spam confidence:",average)