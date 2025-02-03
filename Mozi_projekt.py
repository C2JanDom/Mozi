import random

print("0 = szabadhely, 1 = gyerekjegy, 2 = diák/nyugdíjas jegy, 3 = felnőttjegy")

print("Írja be hány jegyet szeretne: ")
a = int(input())

while a < 2 or a > 5:
    print("Írja be újra hány jegyet szeretne (2 és 5 között): ")
    a = int(input())

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
            if nezoter[i][j] == 3:
                osszeg += 2500
            if nezoter[i][j] == 2:
                osszeg += 2100
            if nezoter[i][j] == 1:
                osszeg += 1300
            if nezoter[i][j] == 0:
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

def egymasMellett(a):
    sor = 0
    if a == 2:
        for i in range(len(nezoter)):
            for j in range(len(nezoter[i])):
                if nezoter[i][j] == 0 and nezoter[i][j-1] == 0:
                    sor = i+1
                    print(sor, "sorba van 2 hely egymás mellett.")
                    return
                
    if a == 3:
        for i in range(len(nezoter)):
            for j in range(len(nezoter[i])):
                if nezoter[i][j] == 0 and nezoter[i][j-1] == 0 and nezoter[i][j-2] == 0:
                    sor = i+1
                    print(sor, "sorba van 3 hely egymás mellett.")
                    return
    
    if a == 4:
        for i in range(len(nezoter)):
            for j in range(len(nezoter[i])):
                if nezoter[i][j] == 0 and nezoter[i][j-1] == 0 and nezoter[i][j-2] == 0 and nezoter[i][j-3] == 0:
                    sor = i+1
                    print(sor, "sorba van 4 hely egymás mellett.")
                    return
                
    if a == 5:
        for i in range(len(nezoter)):
            for j in range(len(nezoter[i])):
                if nezoter[i][j] == 0 and nezoter[i][j-1] == 0 and nezoter[i][j-2] == 0 and nezoter[i][j-3] == 0 and nezoter[i][j-4] == 0:
                    sor = i+1
                    print(sor, "sorba van 5 hely egymás mellett.")
                    return
    if sor == 0:
        print("Nincs")
        return

nezoter_feltoltes()
egymasMellett(a)
bevetel(nezoter)
telitettseg(nezoter)
felnottJegyek(nezoter)