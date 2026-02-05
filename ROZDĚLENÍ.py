with open("cislo.txt", "r") as f:
    radky=f.readlines()
delici=int(input("zadej cislo:"))
with open("mala.txt", "w") as f:
    for i in radky:
        cislo_cs=int(i)
        if cislo_cs<delici:
             f.write(i)
with open("vyhovujici.txt" , "w") as f:
    for i in radky:
        cislo_cs=int(i)
        if cislo_cs>=delici:
             f.write(i)