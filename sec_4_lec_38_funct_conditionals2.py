def string_length(i):
    if type(i) == int:
        return "A number has no length"
    elif type(i) == float:
        return "This is a float, it has no length either"
    else:
        return len(i)
#i = input("Enter a string to see its length: ")

print(string_length(10.0))
