import time
from datetime import datetime


def doopakowania():
    print('do opakowania')

def dekorator(fun):
    def opakowujaca():
        print('przed wywołaniem')
        fun()
        print('po wywołaniu')
    return opakowujaca


@dekorator
def do_opakowania_2():
    print('do opakowania 2')

dek=dekorator(doopakowania)
dek()

do_opakowania_2()


# poczatek = datetime.now()
# to chcemy zliczyc
# koniec = datetime.now()
# print(koniec - poczatek)

# Stwórz funkcję której zadaniem będzie poczekanie 3 sekundy i wypisanie na konsoli komunikatu.
# Dodaj dekorator który zliczy czas wykonywania tej funkcji. Pobranie aktualnego czasu to: "time.time()",
# wstrzymanie na 3 sekundy: "time.sleep(3)"
def dekoruj_cos(fun):
    def liczCzas():
        poczatek = datetime.now()
        fun()
        koniec = datetime.now()
        x = koniec - poczatek
        print(f' wywolanie trwalo {x}')
    return liczCzas


@dekoruj_cos
def opakuj_mnie():
    # time.sleep(3)
    print("Robie ciekawe rzeczy w Pythonie")

@dekoruj_cos
def opakowanie_inne():
    print("inna funkcja")

def trzecia_f():
    print("ja tez cos wypisuje")


# trzecia_f()
# opakowanie_inne()
# opakuj_mnie()

# dekoruj = dekoruj_cos(opakuj_mnie)


# def dekorator_z_parametrem(fun):
#     def wewn(x):
#         print('przed')
#         fun(x)
#         print('po')
#     return wewn
# @dekorator_z_parametrem
# def dekorowana(x):
#     print(f'siema {x}')


def dekorator_z_parametrem(fun):
    def wewn(*args, **kwargs):
        print('przed')
        fun(*args, **kwargs)
        print('po')
    return wewn
@dekorator_z_parametrem
def dekorowana(x):
    print(f'siema {x}')


@dekorator_z_parametrem
def dekorowana_bez_p():
    print(f'siema')


# dekorowana('Andrzej')
# dekorowana(x="Wojtek")
# dekorowana_bez_p()


def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)
    return inner




@percent
@star
def printer(msg):
    print(msg)

# printer("Hello")



# Dodaj dekorator który zliczy czas wykonywania tej funkcji z parametrami. Zaloguj na konsole wszystkie przekazane parametry
def licz_czas_i_loguj(fun):
    def wewnetrzna(*args, **kwargs):
        print(f'Argumenty {args}')
        print(f'Kew-word arguments {kwargs}')
        poczatek = datetime.now()
        fun(*args, **kwargs)
        koniec = datetime.now()
        x = koniec - poczatek
        print(f' wywolanie trwalo {x}')
    return wewnetrzna


@licz_czas_i_loguj
def opakuj_mnie_z_parametrami(x, napis_do_wypisania):
    for i in range(x):
        time.sleep(1)
    print(f"Robie ciekawe rzeczy w Pythonie {napis_do_wypisania}")



# opakuj_mnie_z_parametrami(1,"jestem cool")
# opakuj_mnie_z_parametrami(x=1, napis_do_wypisania="jestem cool jeszcze bardziej")



# dodatkowe materiały o dekoratorach [ENG] https://realpython.com/primer-on-python-decorators/#more-real-world-examples


import functools


@functools.lru_cache()
def fibonacci(num):
    print(f"Calculating fibonacci({num})")
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

# fibonacci(10)
# fibonacci(10)


def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("before Execution")

        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")

        # returning the value to the original frame
        return returned_value

    return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b


# print(sum_two_numbers(2,2))



class Osoba:
    imie = 'Andrzej'
    nazwisko = 'Klusiewicz'
    wiek = 33
    pustePole = None

    def wypiszMnie(self):
        print("Cześć jestem:")
        print(self.imie, self.nazwisko, self.wiek)

    def przywitaj_kolege(self, imie):
        print(f"Cześć {imie} jestem: {self.imie}")


o = Osoba()
print(o.imie, o.nazwisko, o.wiek, o.pustePole)

Osoba().wypiszMnie()

o.imie='Krzysztof'
o.nazwisko='Jarzyna'
print(o.imie,o.nazwisko)

o.wypiszMnie()
o.przywitaj_kolege("Wojtek")

# przywitaj_kolege("Kajetan")

o2 = Osoba()
lista_osob = [o, o2]

for osoba in lista_osob:
    osoba.wypiszMnie()


#     Stwórz klasę "Samochod" posiadającą pola "marka", "model", "rejestracja".
#     Klasa ta powinna zawierać też metodę "wyswietl" wypisującą dane z obiektu na konsoli
#     Stwórz dwa obiekty tej klasy i korzystajac  z metody "wyświetl" wyswietl na konsoli ich zawartość.
class Samochod:
    # marka = None
    # marka = "Renault"
    # model = "Clio"
    # rejestracja = "WE 9001A"

    def __init__(self, marka, model, rejstracja = "DOMYSLNA WARTOSC"):
        self.marka = marka
        self.model = model
        self.rejestracja = rejstracja

    def __str__(self):
        return f'Moj piekny samochodzik: {self.marka}, {self.model}, {self.rejestracja}'
    def wyswietl(self):
        print(f'{self.marka}, {self.model}, {self.rejestracja}')


s1 = Samochod("Opel", "Vectra", "SJZ 11111")
s2 = Samochod("Opel", "Astra")


print(s1)


# Stwórz klasę Zawodnik posiadającą pola wzrost i masa, imie. Pola te mają być uzupełniane przy tworzeniu obiektu.
# Dodaj do klasy metodę get_bmi która zwróci obliczone na podstawie pól BMI.
# Powołaj do życia obiekt tej klasy i wyświetl na konsoli obliczone BMI.
# __str__ - ma wypisac imie, bmi
# wzor na bmi = masa / (wzrost ** 2)   wzrost podany w metrach 1.84
class Zawodnik:

    def __init__(self, wzrost:float, masa:float, imie:str, auto = Samochod("Opel", "Vectra", "SJZ 11111")):
        self._wzrost = wzrost
        self._masa = masa
        self._imie = imie
        self.auto = auto


    def get_bmi(self):
        return self._masa / (self._wzrost ** 2)


    # @classmethod
    # def from_str(cls, linia:str):
    #     dane = linia.strip().split(";")
    #     if len(dane) == 3:
    #         imie, masa, wzrost = dane

    @classmethod
    def from_list(cls, list_zawodnikow):
        lista = []
        for i in range(0, len(list_zawodnikow), 3):
            z = Zawodnik(list_zawodnikow[i], list_zawodnikow[i+1], list_zawodnikow[i+2])
            lista.append(z)
        return lista

    def __str__(self):
        return f'IMIE: {self._imie} BMI: {self.get_bmi():.2f}, jezdzi {self.auto}'   #http://cissandbox.bentley.edu/sandbox/wp-content/uploads/2022-02-10-Documentation-on-f-strings-Updated.pdf

    def __repr__(self):
        return self.__str__()


z1 = Zawodnik(1.80, 75, "Adam", Samochod("Opel", "Astra", "SJZ 22222"))
print(z1)
z2 = Zawodnik(1.85, 80, "Adam")
print(z2)

# slownik = { "Adam" : z1 }
# slownik["Adam"]

# Przeladowanie operatorow https://www.geeksforgeeks.org/operator-overloading-in-python/

dane = [1.8, 70, "Krzysztof", 1.9, 80, "Jerzy"]
lista_z = Zawodnik.from_list(dane)
print(lista_z)



# odczytali dane z pliku dane.txt
# zbudowali sobie liste zawodnikow (jako obietky klasy)
# print tej list

zawodnicy = []
with open("dane.txt", "r") as plik:
    for linia in plik:
        dane = linia.strip().split(";")
        if len(dane) == 3:
            imie, masa, wzrost = dane
            zawodnik = Zawodnik(imie=imie, masa=float(masa), wzrost=float(wzrost))
            zawodnicy.append(zawodnik)

for z in zawodnicy:
    print(z)



# https://realpython.com/python-property/
class Circle:

    def __init__(self, radius):
        self._radius = radius

    def _get_radius(self):
        print("Get radius")
        return self._radius

    def _set_radius(self, value):
        print("Set radius")
        self._radius = value

    def _del_radius(self):
        print("Delete radius")
        del self._radius

    radius = property(
        fget=_get_radius,
        fset=_set_radius,
        fdel=_del_radius,
        doc="The radius property."
    )



class Witacz:
    def powitaj(self,kogo):
        print("No siemka {}!".format(kogo))
    def powitaj(self):
        print("No siemka!")


# w=Witacz()
# w.powitaj()
# w.powitaj("mnie") Tu bedzie bład



from abc import ABC, abstractmethod

class Pisacz:

    def ladnie_pisze(self):
        print("Sobie pisze")



class Rysuje(ABC):

    @abstractmethod
    def narysuje_mnie(self):
        pass

class Figura(ABC):
    def __init__(self, nazwa):
        self.nazwa = nazwa
    def pokaz_nazwe(self):
        print(self.nazwa)

    @abstractmethod
    def oblicz_pole(self):
        pass

# f=Figura()


class Kwadrat(Figura, Rysuje):
    def __init__(self,dlugosc_boku):
        super().__init__('Kwadrat')
        self.dlugosc_boku=dlugosc_boku

    def oblicz_pole(self):
        return pow(self.dlugosc_boku,2)

    def narysuje_mnie(self):
        print("**")
        print("**")



class Prostokat(Figura):
    def __init__(self,bok_a,bok_b):
        super().__init__('Prostokąt')
        self.bok_a=bok_a
        self.bok_b=bok_b
    def oblicz_pole(self):
        return self.bok_a*self.bok_b


kw=Kwadrat(5)
print(kw.nazwa)
print(kw.oblicz_pole())

p = Prostokat(6,8)
# p.ladnie_pisze()

figury =  [Prostokat(2,3), kw, Kwadrat(50), Prostokat(6,8)]

for f in figury:
    f.pokaz_nazwe()
    print(f.oblicz_pole())


# Stwórz klasę abstrakcyjną Restauracja która będzie posiadała abstrakcyjną metodę "serwuj_danie".
# Stwórz klasy "RestauracjaChinska", "RestauracjaWloska" i "RestaruracjaPolska".
# Wymuś posiadanie implementacji metody abstrakcyjnej "serwuj_danie" we wszystkich
# tych klasach ale o różnej implementacji. Powołaj do życia obiekty tych klas,
# a następnie na rzecz każdego z tych obiektów wywołaj funkcję serwuj_danie.

# from abc import ABC, abstractmethod
class Restauracja(ABC):
    @abstractmethod
    def serwuj_danie(self):

        pass

class RestauracjaChinska(Restauracja):
    def serwuj_danie(self):
        """

        Returns
        -------

        """
        print("Restauracja chińska serwuje danie: Kaczka po pekińsku")

class RestauracjaWloska(Restauracja):
    def serwuj_danie(self):
        print("Restauracja włoska serwuje danie: Spaghetti Bolognese")

class RestauracjaPolska(Restauracja):
    def serwuj_danie(self):
        print("Restauracja polska serwuje danie: Bigos")


lista_restauracji = [RestauracjaChinska(), RestauracjaWloska(), RestauracjaPolska()]

for rest in lista_restauracji:
    rest.serwuj_danie()




# Jak zająć programistę?
# - Przeczytaj zdanie poniżej.
# - Przeczytaj zdanie powyżej.







# https://realpython.com/python-with-statement/
from timeit import default_timer as timer
class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.timer = timer

    def __enter__(self):
        self.start = self.timer()
        return self

    def __exit__(self, *args):
        end = self.timer()
        self.elapsed_secs = end - self.start
        self.elapsed = self.elapsed_secs * 1000  # milliseconds
        if self.verbose:
            print('elapsed time: %f ms' % self.elapsed)


#tu bylo troche kodu na start
# with Timer() as t:
#     time.sleep(3)
#     print("Moja bardzo długa funkcja")
#
#
# print(f'Ta funkcja trwała {t.elapsed}')



# https://realpython.com/python-iterators-iterables/


class IncrementIterator:
    def __init__(self, n):
        self.n = n
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.n == self.i:
            raise StopIteration
        self.i += 1
        return self.i


for e in IncrementIterator(10):
    print(e)

class ListaZawodnikow:
    def __init__(self, plik:str):
        self.zawodnicy = []
        self.index = 0
        with open(plik, "r") as plik:
            for linia in plik:
                dane = linia.strip().split(";")
                if len(dane) == 3:
                    imie, masa, wzrost = dane
                    zawodnik = Zawodnik(imie=imie, masa=float(masa), wzrost=float(wzrost))
                    self.zawodnicy.append(zawodnik)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index == len(self.zawodnicy):
            raise StopIteration
        self.index += 1
        # return self.zawodnicy[self.index - 1]
        return f'Zawodnik numer {self.index}, ma BMI {self.zawodnicy[self.index-1].get_bmi()}'


nasza_list = ListaZawodnikow("dane.txt")

zawodnik = next(nasza_list)

for z in nasza_list:
    print(z)

for z in nasza_list:
    print(z)


# Co to jest? Zaczyna się na D, kończy na A i zużywa dużo papieru? - Drukarka hehehe

# Stwórz iterator który będzie zwracał nazwy kolejnych miesięcy. Iterator powinien też posiadać funkcję "restart"
# która spowoduje rozpoczęcie podawania miesięcy od początku.

class MiesiaceIterator:
    def __init__(self):
        self.miesiace = [
            "Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec",
            "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"
        ]
        self.indeks = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indeks < len(self.miesiace):
            miesiac = self.miesiace[self.indeks]
            self.indeks += 1
            return miesiac
        else:
            raise StopIteration

    def restart(self):
        self.indeks = 0

# Użycie iteratora
miesiace_iterator = MiesiaceIterator()

print("Miesiące:")
for i in range(12):
    print(next(miesiace_iterator))

print("\nUruchomienie ponownie:")
miesiace_iterator.restart()
for i in miesiace_iterator:
    print(i)