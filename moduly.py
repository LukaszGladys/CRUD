import math

slowniki = []


def create():
    while True:
        rekord = {"id": [], "imie": [], "nazwisko": [], "pesel": []}
        x = int(input("\n1 - wczytaj dane z pliku tekstowego\n2 - wpisanie wartości ręcznie\n3 - cofnij\n"))
        if x == 1:
            f = open("data.txt", mode='r', encoding='utf-8')
            znak = f.readline()
            while znak:
                id, imie, nazwisko, pesel = znak.strip().split(';')
                rekord = {
                    "id": int(id),
                    "imie": imie,
                    "nazwisko": nazwisko,
                    "pesel": pesel
                }
                x = 0
                for slownik in slowniki:
                    if slownik["id"] == rekord["id"]:
                        x = 1
                        print("Rekord o ID:", slownik["id"], "już istnieje!!!")
                if x == 0:
                    slowniki.append(rekord)
                    print("Wczytano rekord o ID", rekord["id"],"do bazy danych")
                znak = f.readline()
            f.close()

        elif x == 2:
            id = int(input("\nPodaj id\n"))
            jest = False
            for slownik in slowniki:
                if slownik["id"] == id:
                    jest = True
            if len(slowniki) == 0 or jest == False:
                imie = str(input("\nPodaj imie\n"))
                imie = imie.lower()
                imie = imie.capitalize()
                nazwisko = str(input("\nPodaj nazwisko\n"))
                nazwisko = nazwisko.lower()
                nazwisko = nazwisko.capitalize()
                while True:
                    pesel = str(input("\nPodaj pesel\n"))
                    if len(pesel) == 11:
                        break
                    else:
                        print("Zła wartość numeru PESEL!!!")
                rekord["id"].append(id)
                rekord["imie"].append(imie)
                rekord["nazwisko"].append(nazwisko)
                rekord["pesel"].append(pesel)
                rekord["id"] = id
                rekord["imie"] = imie
                rekord["nazwisko"] = nazwisko
                rekord["pesel"] = pesel
                slowniki.append(rekord)
                print("DODANO REKORD o ID:",id)
            else:
                print("Rekord o podanym ID istnieje!")

        elif x == 3:
            break
        else:
            print("WYBIERZ POPRAWNĄ CYFRĘ!")


def read():
    print("| id || ", end="")
    print("imie || ", end="")
    print("nazwisko || ", end="")
    print("pesel | ")
    print("----------------------------------")

    for slownik in slowniki:
        print("|", slownik["id"], "|", end="")
        print("|", slownik["imie"], "|", end="")
        print("|", slownik["nazwisko"], "|", end="")
        print("|", slownik["pesel"], "|")


def update():
    zmiana = int(input("Podaj ID rekordu, który chcesz zmienić\n"))
    jest = False
    for slownik in slowniki:
        if slownik["id"] == zmiana:
            jest = True
            wybor = int(input("\nCo chcesz zaktualizować?\n1 - imie\n2 - nazwisko\n3 - pesel\n"))

            if wybor == 1:
                n_imie = str(input("Podaj nowe imie:\n"))
                n_imie = n_imie.lower()
                n_imie = n_imie.capitalize()
                slownik["imie"] = n_imie
                print("Imię dla rekordu o id =", zmiana, "zmienione")

            elif wybor == 2:
                n_nazwisko = str(input("Podaj nowe nazwisko:\n"))
                n_nazwisko = n_nazwisko.lower()
                n_nazwisko = n_nazwisko.capitalize()
                slownik["nazwisko"] = n_nazwisko
                print("Nazwisko dla rekordu o id =", zmiana, "zmienione")
            elif wybor == 3:
                n_pesel = int(input("Podaj nowy pesel:\n"))
                slownik["pesel"] = n_pesel
                print("Pesel dla rekordu o id =", zmiana, "zmienione")
            else:
                print("Wybierz poprawną cyfrę !")
    if not jest:
        print("\nREKORD O PODANYM ID NIE ISTNIEJE !!!")


def delete():
    x = int(input("Podaj id rekordu, który chcesz usunąć\n"))
    istnieje = 0
    for slownik in slowniki:
        if slownik["id"] == x:
            slowniki.remove(slownik)
            istnieje = 1
            print("Rekord usunięty")
    if istnieje == 0:
        print("REKORD O PODANYM ID NIE ISTNIEJE !!!")


def srednia():
    if len(slowniki) == 0:
        print("BAZA DANYCH JEST PUSTA!!!")
    else:
        j = 0
        suma = 0
        for slownik in slowniki:
            s = slownik["pesel"]
            s = str(s)
            stulecie = int(s[2])*10 + int(s[3])
            if stulecie > 0 and stulecie < 13:
                rocznik = 1900 + int(s[0])*10 + int(s[1])
                wiek = 2021 - rocznik
                suma = suma + wiek
                j = j+1
            elif stulecie > 20 and stulecie < 33:
                rocznik = 2000 + (stulecie-20)
                wiek = 2021 - rocznik
                suma = suma + wiek
                j = j + 1
            elif stulecie > 80 and stulecie < 93:
                rocznik = 1800 + int(s[0]) * 10 + int(s[1])
                wiek = 2021 - rocznik
                suma = suma + wiek
                j = j + 1
        srd = suma/j
        print("Średnia wieku osób w bazie danych wynosi:",round(srd,2),"lat.")


def liczba():
    if len(slowniki) == 0:
        print("BAZA DANYCH JEST PUSTA!!!")
    else:
        kobiety = 0
        mezczyzni = 0
        for slownik in slowniki:
            s = slownik["pesel"]
            s = str(s)
            p = int(s[9])
            if p % 2 == 0:
                kobiety = kobiety+1
            else:
                mezczyzni = mezczyzni+1
        print("Liczba mezczyzn to:", mezczyzni)
        print("Liczba kobiet to:", kobiety)