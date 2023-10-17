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
