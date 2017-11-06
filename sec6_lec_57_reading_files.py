'''
f= open("files/fruits.txt")

for i in f:
    i = i.rstrip("\n")
    print i
f.close()
'''

f = open("files/fruits.txt","r")
i = f.readlines()
for t in i:
    print(len(t) - 1)