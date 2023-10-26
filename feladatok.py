def elso():
    szam = 0
    while szam < 149:
        if szam % 2 == 0:
            print(szam, end=",")
        szam += 1
    print(150, end="")


def masodik():
    i = 0
    while i < 11:
        i += 1
        szam = int(input("Kérem adjon meg egy számot!"))
        if szam % 3 == 0:
            print("Ez a szám hárommal oszthetó: "+str(szam))
        else:
            print("Ez a szám nem osztható hárommal: "+str(szam))


def harmadik():
    szam = int(input("Kérem adjon meg egy számot!"))
    while not szam % 10 == 0:
        szam = int(input("Kérem adjon meg egy számot!"))
    print("Gratulálunk! Nyert egy gucci táskát!")


def negyedik():
    szam = int(input("Kérem adjon meg egy számot!"))
    while not ((szam % 2 == 0) and (szam > 9) and (szam < 100)):
        szam = int(input("Kérem adjon meg egy számot!"))
    print("Ez a szám kétjegyü, és páros: "+str(szam))

def otodik():
        szam = int(input("Kérem adjon meg egy számot!"))
        while not ((szam % 2 == 1) and (szam > 0)):
            szam = int(input("Kérem adjon meg egy számot!"))
        print("Ez a szám pozitív és páratlan: " + str(szam))

import math


def hatodik():
    szam = int(input("Kérem adjon meg egy számot!"))
    gyok = math.sqrt(szam)
    while not ((szam % 3 == 0) or (round (gyok)==gyok)):
        szam = int(input("Kérem adjon meg egy számot!"))
    print("Ez a szám 3-mal osztható vagy négyzetszám: " + str(szam))


def hetedik():
    a = int(input("Kérem adjon meg egy számot!"))
    b = int(input("Kérem adjon meg egy számot!"))
    c = int(input("Kérem adjon meg egy számot!"))
    while not ((a+b)>c and (a+c)>b and (b+c)>a):
        a = int(input("Kérem adjon meg egy számot!"))
        b = int(input("Kérem adjon meg egy számot!"))
        c = int(input("Kérem adjon meg egy számot!"))
    print("Szerkeszthető a háromszög")


def nyolcadik():
    szoveg = str(input("Kérem írjon be egy szöveget!"))
    while not (len(szoveg) >= 3): # len(valtozo) >=3-- a szöveg karaktereinek száma
        szoveg = str(input("Kérem írjon be egy szöveget!"))
    print(szoveg.upper())  # valtozo.upper()-nagybetuvel kiirja a valtozot

def kilencedik():
    szoveg = str(input("Kérem írjon be egy szöveget!"))
    while not (len(szoveg) >= 4):  # len(valtozo) >=4-- a szöveg karaktereinek száma
        szoveg = str(input("Kérem írjon be egy szöveget!"))
    print(szoveg.lower()) # valtozo.upper()-kisbetuvel kiirja a valtozot


def tizedik():
    global atlag
    print("Kérem adja meg a számokat, amiknek az átlagát szeretné kiszámolni!\n0-val jelezheti, hogy a kívánt számokat megadta")
    szam=int(input("Adja meg a számot!"))
    eredmeny = 0
    sorszam = 0
    while not szam == 0:
        eredmeny += szam
        sorszam += 1
        atlag = eredmeny/sorszam
        szam = int(input("Adja meg a számot!"))
    print("A megadot számok átlaga: "+str(round(atlag, 2))) # két tizedesjegy??


def tizenegyedik():
    global atlag
    print(
        "Kérem adja meg azokat a pozitív számokat, amiknek az átlagát szeretné kiszámolni!\n0-val jelezheti, hogy a kívánt számokat megadta")
    szam = int(input("Adja meg a számot!"))
    eredmeny = 0
    sorszam = 0
    while not (szam == 0):
        while szam < 0:
            szam=int(input("Ez a szám negatív, kérem adjon meg pozitív számokat!"))
        eredmeny += szam
        sorszam += 1
        szam = int(input("Adja meg a számot!"))

    atlag = eredmeny / sorszam
    print("A megadot számok átlaga: " + str(round(atlag, 2)))  # két tizedesjegy??