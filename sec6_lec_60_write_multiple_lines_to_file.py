numbers = [1, 2, 3]

file=open("files/sec6lec60.txt","w")

for i in numbers:
    file.write(str(i) + "\n")

file.close()