import os

def foglalas():
    nev = input("Vendég neve: ")
    kezdete = input("Foglalás kezdete (HÓNAP-NAP ÓRA:PERC formátumban): ")
    vege = input("Foglalás vége (ÓRA:PERC formátumban): ")
    szekek = input("Foglalt székek száma: ")
    hely = input("Beltéri vagy kültéri asztalt szeretnének (B = beltéri, K = kültéri): ")

def torles():
    print("Foglalás törlése")

def statisztika():
    print("Statisztika")

def main():
    opciok = None
    print("Menü:\n")
    print("1. Foglalás")
    print("2. Foglalás törlése")
    print("3. Statisztika")
    print("4. Kilépés\n")

    while True:
        opciok = input("1/2/3/4: ")
        if opciok == "1":
            foglalas()
        elif opciok == "2":
            torles()
        elif opciok == "3":
            statisztika()
        elif opciok == "4":
            print("Viszlát!")
        else:
            continue
        break

if __name__ == "__main__":
    main()