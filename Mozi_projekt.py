import random

nezoter=[]

def nezoter_feltoltes():
    for i in range(15):
        sorok=[]
        for i in range(10):
            sorok.append(random.randint(0,3))
        sorok.append("---")
        for i in range(10):
            sorok.append(random.randint(0,3))
        print(sorok)
        nezoter.append(sorok)

def bevetel(nezoter):
    osszeg = 0
    for i in range(len(nezoter)):
        for j in range(len(nezoter[i])):
            if nezoter[i][j] == 0:
                osszeg += 2500
            if nezoter[i][j] == 1:
                osszeg += 2100
            if nezoter[i][j] == 2:
                osszeg += 1300
            if nezoter[i][j] == 3:
                osszeg += 0
    print("Az összes bevétel: ",osszeg, "Ft")

def telitettseg(nezoter):
    feltoltottUlohely=300
    for i in range(len(nezoter)):
        for j in range(len(nezoter[i])):
            if nezoter[i][j] == 0:
                feltoltottUlohely -= 1

    print("A terem kihasználtsága", round(feltoltottUlohely/300*100, 2),"%.")

def felnottJegyek(nezoter):
    felnottjegyek = 0
    for i in range(len(nezoter)):
        for j in range(len(nezoter[i])):
            if nezoter[i][j] == 3:
                felnottjegyek += 1

    print("Az összes felnőtt jegy száma:",felnottjegyek, "db")

nezoter_feltoltes()
bevetel(nezoter)
telitettseg(nezoter)
felnottJegyek(nezoter)