import datetime
#import glob2



#Create empty file

filename=datetime.datetime.now()
lst = ["files/sec7lec72/file1.txt", "files/sec7lec72/file2.txt", "files/sec7lec72/file3.txt"]

def read_files():
    for i in lst:
        f = open(i, "r")
        i = f.read()
        f.close()
        print (i)

def create_file_fill():
    with open("files/" + filename.strftime("%Y-%m-%d-%H-%M-%s") + ".txt", "w") as file:
        file.write("")
        for i in lst:
            f = open(i, "r")
            i = f.readlines()
            file.write(str(i) + "\n")

        file.close()



create_file_fill()
read_files()


'''
filenames = glob2.glob("files/sec7lec72/*.txt")

with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%s") + ".txt") as file:
    for filename in filenames:
        with open (filename, "r") as f:
            file.write(f.read() + "\n")
'''