#mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#print(mylist[2])

import datetime

"""
This script creates an empty file.
"""

filename = datetime.datetime.now()

#Create empty file
def create_file():
    """ This function creates an empty file"""

    with open ("files/" + filename.strftime("%Y-%m-%d-%H-%M") + ".txt","w") as file:
        file.write("")

create_file()