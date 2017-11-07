def string_length(i):
    if type(i) == int:
        return "A number has no length"
    else:
        return len(i)
#i = input("Enter a string to see its length: ")

print(string_length("supercalifragalisticexpiallydocious"))
