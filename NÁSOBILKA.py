import random
p=int(input("zadej cislo pokusu"))
nah1=random.randint(2,10)
nah2=random.randint(2,10)
nas=0
nas=nah1*nah2
print(nah1,"*",nah2)
od=int(input("kolik se rovna"))
if od==nas:
    print("skvele")
else:
    print("chiba")
