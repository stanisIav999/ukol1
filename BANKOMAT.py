zbytek=0
def zapis_do_souboru(castka):
    with open("ucett.txt", "w") as f:
        f.write (str(castka)+"\n")
def vklad():
    a=int(input("zadej castku"))
    zapis_do_souboru(a)

def vyber():
    b=int(input("zadej castku"))
    zapis_do_souboru(b)

def zustatek():
    kolik=0
    with open("ucett.txt", "r") as f:
        for radek in f:
            cs=int(radek)
            kolik=kolik+cs
    return kolik
while True:
    uzivatel=int(input("1-vklad, 2-vyber, 3 zustatek, 0-konec"))
    if uzivatel==1:
        vklad()
    if uzivatel==2:
        vyber()
    if uzivatel==3:
        zbytek=zustatek()
        print("zustatek je", zbytek)