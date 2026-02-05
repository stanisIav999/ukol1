import  random
nah=random.randint(1,100)
pocet=0
while True:
    cs = int(input("Zadej cislo:"))
    pocet=pocet+1
    if cs == nah:
        break
    elif cs < nah:
        print("won")

    else:
        print("lose")
print("uhodnuto na",pocet,"pokusu")