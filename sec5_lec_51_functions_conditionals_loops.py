temperatures=[10,-20,-289,100]
def conv_cel_deg(c):
    f = (c * 9/5) + 32

    if (f <= -273.15):
        return "Coldest possible temperture is -273.15 (Absolute Zero), try again"
    else:
        return (f)

for t in temperatures:
    print(conv_cel_deg(t))