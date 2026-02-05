heslo=input("zahadej jmeno")
heslo2=input("zahadej heslo")
nasel=False
with open("seznam.txt", "r") as f:
 for i in f:
    i=i.strip()
    pole=i.split(";")
    if pole[0]==heslo:
        if pole[1]==heslo2:
           nasel=True
if nasel:
    print("pristup povolen")
else:
    print("pristup nepovolen")