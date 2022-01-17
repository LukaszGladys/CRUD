import moduly

while True:
    wybor = int(input("\nWitaj! Co chcesz zrobić?\n\n1 - stworzenie bazy danych\n2 - odczytanie bazy danych\n3 - "
                      "aktualizcja bazy danych\n4 - usunięcie rekordu z bazy danych\n5 - średnia wieku osób "
                      "w bazie danych\n6 - liczba kobiet oraz mężczyzn\n7 - wyjście\n"))
    if wybor == 1:
        moduly.create()
    elif wybor == 2:
        moduly.read()
    elif wybor == 3:
        moduly.update()
    elif wybor == 4:
        moduly.delete()
    elif wybor == 5:
        moduly.srednia()
    elif wybor == 6:
        moduly.liczba()
    elif wybor == 7:
        break
    else:
        print("WYBIERZ POPRAWNĄ CYFRĘ!")
