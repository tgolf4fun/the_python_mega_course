
temperatures = [10, -20, -289, 100]


def writer(temperatures):
    with open("files/sec6lec66.txt", "w") as file:
        for t in temperatures:
            if t > -273.15:
                t = t*9/5 + 32
                file.write(str(t) + "\n")

writer(temperatures)