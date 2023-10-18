import operator
import random
import os
import re
from collections import defaultdict

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
        """
        Ta funckja zajmuje sie znajdowaniem katalowgo i plikow. Ignoruje wielkosci liter
        Parameters
        ----------
        katalog_startowy
        fraza

        Returns
        -------

        """
        znalezione_elementy = []

        fraza = fraza.lower()

        for root, dirs, files in os.walk(katalog_startowy):
            for element in dirs + files:
                if fraza in element.lower():
                    znalezione_elementy.append(os.path.join(root, element))

        print(znalezione_elementy)

    # znajdz_pliki_i_katalogi(folder_startowy, szukna_fraze)

    help(znajdz_pliki_i_katalogi)
    print(znajdz_pliki_i_katalogi.__doc__)

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


    # Napisz system który zwróci nam ilość wystąpień każdego ze słow w pliku
    # Nazwa pliku ma zostać przekazana przez  zmienną.
    # Wynik powinien byc posortowany malejąco wg ilosci wystapien
    # a) odczytaj wszystkie linie z pliku i rozbij na słowa. Każde ze słów dodaj jako elemnt listy.
    # Zadbaj o usunięcie po drodze znaków specjalnych czyli kropek, przecinków, wykrzykników
    # etc.

    # b) stwórz słownik i dla każdego słowa w liście sprawdz czy istnieje juz wpis dotyczący tego
    # słowa
    # w słowniku. Jeśli nie ma to dodaj do słownika wpis o kluczu takim jak sprawdzane słowo i
    # wartości 1
    # dla ilości wystąpień. Jeśli takie słowo pojawia się już w kluczach słownika to trzeba
    # zwiększyc wartośc o 1


    # c) Przepakuj dane ze słownika do listy i posortuj.

    nazwa_pliku = "text.txt"

    wystapienia = {}
    # Defining the dict
    wystapienia2 = defaultdict(int)  #    from collections import defaultdict

    with open(nazwa_pliku, "r", encoding='utf-8') as plik:
        # while True:
        #     linia = plik.readline()
        #     if not linia:
        #         break
        for linia in plik:
            linia_wyczyszczona = re.sub(r'\W+', ' ', linia)   # https://www.w3schools.com/python/python_regex.asp
            slowa = linia_wyczyszczona.lower().split()
            for slowo in slowa:
                if slowo in wystapienia:            # https://www.geeksforgeeks.org/defaultdict-in-python/
                    wystapienia[slowo] += 1
                else:
                    wystapienia[slowo] = 1

                wystapienia2[slowo] += 1

    print(wystapienia)

    posortowane_wystapienia = sorted(wystapienia.items(), key=lambda x: x[1], reverse=True)
    posortowane_wystapienia2 = sorted(wystapienia.items(), key=operator.itemgetter(1), reverse=True)
    print(posortowane_wystapienia)


    def razy2(a:int) -> int:  # funkcja która będzie użyta jako argument
        return a * 2

    def funkcja_jako_argument(f, x):
        print(f(x))


    funkcja_jako_argument(razy2, 33)
    funkcja_jako_argument(lambda x: x+1, 1)


    def powieksz(x:str):
        return x.upper()

    def tytul(napis:str) -> str:
        return napis.title()

    def zastosuj_dla_wszystkich(fun, *args):
        for a in args:
            print(fun(a))

    zastosuj_dla_wszystkich(powieksz, 'siała', 'baba', 'mak')
    zastosuj_dla_wszystkich(tytul, 'siała', 'baba', 'mak',)



    #     • Stwórz funkcję która wydrukuje na konsoli sumę wartości przekazanych do niej jako *args

    def moja_suma(*argumenty):
        suma = 0
        for i in argumenty:
            suma += i
        return suma

    print(moja_suma(1,2,3,4,5,6,7,8,9,10))


    #     • (rozne typy argumentow)Stwórz funkcję która przyjmie nieokreśloną liczbę elementów przez argument,
    #     a następnie wypisze na konsoli ilość otrzymanych elementów. Poniżej informacji o ilości
    #     otrzymanych elementów wyświetl w osobnych liniach każdy argument oraz jego typ.

    def wiele_argumentów(*args):
        ile_ich = len(args)
        print(ile_ich)
        for element in args:
            print(element, type(element))


    wiele_argumentów([1], "abc", 1.0, 123, "Moj super kurs pythona")


    def my_sum(a, b, c):
        print(a + b + c)

    my_list = [1, 2, 3]
    my_sum(*my_list)


    def my_sum(*args):
        result = 0
        for x in args:
            result += x
        return result


    list1 = [1, 2, 3]
    list2 = [4, 5]
    list3 = [6, 7, 8, 9]

    print(my_sum(*list1, *list2, *list3))


    def pomnoz_razy_dwa(x):
        return x * 2
    def podziel_przez_trzy(x):
        return x / 3
    def dodaj_piec(x):
        return x + 5

    funkcje = [pomnoz_razy_dwa, podziel_przez_trzy, dodaj_piec]
    def obrob(wartosc, *funkcs):
        for f in funkcs:
            wartosc = f(wartosc)
        return wartosc

    print(obrob(1, pomnoz_razy_dwa, podziel_przez_trzy, dodaj_piec))


    def zewnetrzna(x):
        def wewnetrzna(x):
            return x * 2
        print(wewnetrzna(x))
        return 1

    zewnetrzna(25)

    def czytaj_pdf(plik):
        print("czytam pdf")

    def czytaj_xml(plik):
        print("czytam xml")

    dekodawnie_plikow = {
        ".pdf" : czytaj_pdf,
        ".xml" : czytaj_xml
    }
    wspierane = list(dekodawnie_plikow.keys())

    for plik in os.listdir("."):
        rozszerzenie = os.path.splitext(plik)[1]
        if rozszerzenie in wspierane:
            dekodawnie_plikow[rozszerzenie](plik)

    pomnoz_razy_dwa(x=2)



    def parametr_kwargs(**kwargs):
        for k in kwargs:
            print(k, kwargs[k])

    parametr_kwargs(dodatkowy=48, nastepny=111)



    def zapisz_parametry_do_pliku(nazwa_pliku, **parametry):
        plik = open(nazwa_pliku, mode='w', encoding='utf-8')
        for p in parametry:
            plik.write(f'{p};{parametry[p]}\n')
        plik.close()

    zapisz_parametry_do_pliku('mojplik.csv', parametr1='wartość 1', parametr2=2, moj_argument="Jestesmy zmeczeni bardzo")

    from datetime import datetime
    import time

    def czekacz():
        time.sleep(1)
        return 1

    # poczatek = datetime.now()
    # for x in range(10):
    #     czekacz()
    # koniec = datetime.now()
    # print(koniec - poczatek)


    import functools


    # @functools.lru_cache(maxsize=None)
    # def czekacz():
    #     time.sleep(1)
    #     return 1
    #
    # poczatek = datetime.now()
    # for x in range(10):
    #     czekacz()
    # koniec = datetime.now()
    # print(koniec - poczatek)


    # Stworz funkcje "config" ktora bedzie otrzymywala argumenty kwargs bedace ustawieniami.
    # Funkcja ta ma zapisac podane argumenty do pliku config.csv w 2 kolumnach z czego pierwsza jest nazwa
    # argumentu a druga jego wartoscia. Jesli dane argument juz istnieje w pliku to trzeba bedzie tylko zaktualizowac
    # jego wartosc, jesli jeszcze go nie ma to trzeba go bedzie dodac do pliku.
    def config(nazwa_pliku, **parametry):
        wczytany_config = {}
        with open(nazwa_pliku, mode='r', encoding='utf-8') as plik:
            for linia in plik:
                klucz, wartosc = linia.split(';')
                wczytany_config[klucz] = wartosc

        for p in parametry:
            wczytany_config[p] = parametry[p]

        plik = open(nazwa_pliku, mode='w', encoding='utf-8')
        for p in wczytany_config:
            plik.write(f'{p};{wczytany_config[p]}\n')
        plik.close()

    # config("plik.csv", wersja=1, arg=2, argument321 = 3)
    # config("plik.csv", arg_inny=2, argument321=3, wersja=2.0)

    #funckja w funkcji
    # Napisz funkcje która będzie tworzyła listę liczb parzystych lub nieparzystych w danym zakresie
    # funkcje do sprawdzenia parzystosci napisz jako funckje wewnętrzne i w zależności
    # od przekazanego parametru wywołuj odpowiednią
    def generuj_liczby(start:int, koniec:int, parzyste:bool = True):

        def parzysta(x:int) -> bool:
            return x % 2 == 0

        def nieparzysta(x:int) -> bool:
            return x % 2 == 1

        list_liczba = []
        for i in range(start,koniec):
            if parzyste and parzysta(i):
                list_liczba.append(i)
            elif not parzyste and nieparzysta(i):
                list_liczba.append(i)

        return list_liczba

    print(generuj_liczby(0,20,parzyste=False))

    print(generuj_liczby(parzyste=True, koniec=100, start=10))

    print(generuj_liczby(10, parzyste=True, koniec=100))
    print(generuj_liczby(10, 100, True))

    print(range(10000000000000))


    def elementy():
        yield 'element numer 1'
        yield 'element numer 2'
        yield 'element numer 3'
        yield 'element numer 4'

    gen = elementy()


    for e in elementy():
        print(e)

    def potegi2(n):
        for x in range(1, n + 1):
            yield pow(2, x)

    for p in potegi2(50):
        print(p)


    def dziesieci():
        i = 1
        while True:
            yield i * 10
            i += 1


    dz = dziesieci()
    print(dz.__next__())
    print(dz.__next__())
    print(dz.__next__())

    potegi22 = [2 ** i for i in range(100)]
    generator_potegi = (2 ** i for i in range(100000))
    print(generator_potegi)
    next(generator_potegi)
    generator_potegi.__next__()

    # print(generator_potegi[5])

    for i in generator_potegi:
        print(i)
        if i > 2048:
            break

    # for i in dziesieci():
    #     print(i)

    #  Stworz generator ktory bedzie przyjmowal przez parametr ilosc elementow a nastepnie zwracal elementy o tresci
    #  'element o indeksie x'( gdzie x bedzie numerem podawanego elementu) czekajac 1 sekunde przed zwrotem kazdego elementu.
    def generator_elementów(ilosc:int):
        for i in range(ilosc):
            # time.sleep(1)
            yield f'element o indeksie {i}'
            # yield print(f'element o indeksie {i}')

    genrator = generator_elementów(3)
    print(next(genrator))
    next(genrator)
    print(next(genrator))



    #     Stwórz generator który będzie podawał nieskończenie wiele liczb parzystych.
    #     Przetestuj go pobierając z niego kolejne wartości i wyświetlając je na konsoli.
    def  generator_parzysty():
        i = 0
        while True:
            yield i
            i += 2

    for i in generator_parzysty():
        print(i)
        if i > 20:
            break


