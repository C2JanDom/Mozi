import random

nezoter=[]

def nezoter_feltoltes():
    for i in range(15):
        for n in range(10):
            nezoter.append(random.randint(0,3))
        for n in range(1):
            nezoter.append("---")
        for n in range(10):
            nezoter.append(random.randint(0,3))

    print(nezoter)

def bevetel(a):
    osszeg = 0
    felnottAr = 2500
    diakNyugdijasAr = 2100
    gyerekAr = 1300
    szabadUlohelyAr = 0
    for i in range(nezoter):
        if a == 0:
            osszeg += felnottAr
        if a == 1:
            osszeg += diakNyugdijasAr
        if a == 2:
            osszeg += gyerekAr
        if a == 3:
            osszeg += szabadUlohelyAr

def telitettseg(a):
    feltoltottUlohely=300
    for i in range(nezoter):
        if a == 0:
            feltoltottUlohely -= 1

def felnottJegyek(a):
    felnottjegyek = 0
    for a in range(nezoter):
        if a == 3:
            felnottjegyek += 1
    print(felnottjegyek)

print(nezoter_feltoltes())