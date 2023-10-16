import random
import os

def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    # print_hi('Pyton Kurs')

    tablica = [1,23,43543]
    # tab = list()

    tablica.append(2)
    tablica.insert(1, 3432)

    # print(f'Element {tablica[0] + tablica[1]}, ostatni element list {tablica[-1]}')

    # print(tablica)
    # for i in tablica:
    #     print(i)

    # for i in range(0,10):
    #     print(i)

    # Napisz kod który umieści w liście 10 kolejnych potęg liczby 2.
    dwa_do_drugiej = 2 ** 2

    potegi = []
    for i in range(1,11):
        x = 2 ** i
        potegi.append(x)
        # potegi.insert(i, 2 ** i)

    # print(potegi)

    poloczone_list = potegi + tablica
    # alternatywa
    potegi += tablica   # poloczone_list = poloczone_list + tablica

    print(poloczone_list)
    print(potegi)
    print(tablica)

    # for element in tablica:
    #     potegi.append(element)
    potegi.extend(tablica)

    # print(potegi)
    # potegi.append(tablica)
    # print(potegi)

    x = random.randint(1,10)

    # Stwórz dwie listy. Każda z list ma zawierać 10 liczb losowych z zakresu 1-10. Połącz te dwie
    # listy do jednej i wyswietl na konsoli (extend albo *lista)
    list1 = []
    list2 = [] # list()
    for i in range(10):
        list1.append(random.randint(0, 10))
        list2.append(random.randint(0, 10))

    wynik = list1 + list2
    list1.extend(list2)
    print(wynik)
    print(list1)

    list_poteg = [[2,4], [3,8]]
    print(list_poteg)
    # Korzystajac z petli stworz liste zawierajaca elementy same bedace listami. Kazdy taki
    # element ma zawierac numer potegi oraz wartosc tej potegi dla liczby 2.
    lista_list = []
    for i in range(10):
        lista_list.append([i, 2 ** i])
    print(lista_list)

    poszukiwani=["Michael Scofield","Lincoln Burrows","TheodoreBagwell","Uczciwy polityk", "Andrzej Klusiewicz"]
    if("Andrzej Klusiewicz" in poszukiwani):
        print("pszypau")
    else:
        print("nie pszypau")

    # potegi[0] = 321
    # print(potegi)

    # [2, 4, 8, 16, 32, 64,]
    # [0, 1, 2, 3, 4, 5,]
    # print(potegi[2:4])
    # print(potegi[:4])
    # print(potegi[4:])
    # print(potegi[1:-1])

    # napis = "napis"
    # print(napis[1:-1:2])
    # print(napis[::-1])

    # napis = "napis-123-deprtament"
    # podzielone = napis.split("-")
    # print(podzielone)
    # numer = int(podzielone[1])
    # print(numer)
    #
    # litery = list(napis)
    # print(litery)
    # lokalizacje = litery.index('-')
    # print(lokalizacje)

    potegi.sort()
    potegi.reverse()
    print(potegi)

    # list3 = []
    # for i in range(10):
    #     list3.append(random.randint(0, 10))

    list3 = [random.randint(0,10) for i in range(10)]
    print(list3)

    przefiltrowana = [element for element in list3 if element > 5]
    print(przefiltrowana)

    # Korzystając z list składanych wygeneruj listę zawierajaca 10 kolejnych poteg 2
    lista_poteg_2 = [2 ** i for i in range(10)]
    print(lista_poteg_2)

    # wynik = os.walk(".")
    # print(wynik)

    # for root, dirs, files in os.walk("."):
    #     for name in files:
    #         print(os.path.join(root, name))
    #     for name in dirs:
    #         print(os.path.join(root, name))

    # Napisz wyszukiwarkę plików która
    # przyjmie od użytkownika szukaną frazę i katalog startowy. Wyszukiwarka ma wyswietlić
    # wszystkie pliki i katalogi zawierajace w nazwie szukaną frazę - wraz ze ścieżkami.
    # Wyszukiwarka ma być nieczuła na wielkość liter

    folder_startowy = "."
    szukna_fraze = ".txt"

    # folder_startowy = input("Podaj folder startowy ")
    # szukna_fraze = input("Podaj szukna_fraze ")

    def znajdz_pliki_i_katalogi(katalog_startowy, fraza):
        znalezione_elementy = []

        fraza = fraza.lower()

        for root, dirs, files in os.walk(katalog_startowy):
            for element in dirs + files:
                if fraza in element.lower():
                    znalezione_elementy.append(os.path.join(root, element))

        print(znalezione_elementy)

    # znajdz_pliki_i_katalogi(folder_startowy, szukna_fraze)


    ############################### Krotki - tuple
    krotka = ("Imie", 23, 2.3)
    print(krotka)
    print(krotka[0])

    dni_tygodnia = ("poniedziałek", "wtorek")

    def funkcja():
        return ("wynik", 321, "sciekza")

    w = funkcja()
    napis, liczba, sciezka = funkcja()
    liczba += 1
    # w[1] += 1   # error
    print("")

    krotka = tuple(random.randint(0,10) for i in range(10))
    print(krotka)
    lista_z_krotki = list(krotka)
    print(lista_z_krotki)
    krotka_z_listy = tuple(lista_z_krotki)
    print(krotka_z_listy)

    # https://www.geeksforgeeks.org/namedtuple-in-python/

    slownik = {}
    slownik2 = dict()

    info = {
        "LG123" : "Telewizor 60' z HD Ready, wejściem na internety ifiltrem reklam",
        "SONY666" : "Piekielnie dobry telewizor",
        "SZAJSUNG999" : "Telewizor świetnie nadający się do zakrycia dziury w ścianie(i niczego więcej)"
    }

    print(info)
    print(info["LG123"])
    print(info.keys())
    print(info.values())

    for i in info:
        print(info[i])

    for k in info.keys():
        print(info[k])

    if "LG123" in info:
        print("Mamy taki produkt")
    else:
        print("niet :(")

    info["KLUCZ"] = "WARTOŚĆ"

    # wczytaj dane do słownika w ten sposób by pierwsza kolumna stanowila klucze a
    # druga przypisane do nich wartości. Przeiteruj po słowniku i wypisz klucze oraz przypisane do nich wartości

    # plik = open("ustawienia.txt", "r")
    # #tutaj czytanie pliku
    # plik.close()

    ustawienia = {}

    with open("ustawienia.txt", "r") as plik:
        for linia in plik:
            linia = linia.strip().split(';')
            if len(linia) == 2:
                klucz, wartosc = linia
                ustawienia[klucz] = wartosc

    for k, v in ustawienia.items():
        print(f'Klucz: {k}, wartosc: {v}')


    # Napisz system który zwróci nam ilość wystąpień każdego ze słow w pliku w postaci listy krotek.
    # [ (slowo,ilosc_wystapien),(slowo,ilosc_wystapien) ]. Nazwa pliku ma zostać przekazana przez  zmienną.
    # Wynik powinien byc posortowany malejąco wg ilosci wystapien
    # a) odczytaj wszystkie linie z pliku i rozbij na słowa. Każde ze słów dodaj do osobnej listy.
    # Zadbaj o usunięcie po drodze znaków specjalnych czyli kropek, przecinków, wykrzykników
    # etc.


    # b) stwórz słownik i dla każdego słowa w liście sprawdz czy istnieje juz wpis dotyczący tego
    # słowa
    # w słowniku. Jeśli nie ma to dodaj do słownika wpis o kluczu takim jak sprawdzane słowo i
    # wartości 1
    # dla ilości wystąpień. Jeśli takie słowo pojawia się już w kluczach słownika to trzeba
    # zwiększyc wartośc o 1


    # c) Przepakuj dane ze słownika do listy i posortuj.