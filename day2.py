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
    time.sleep(3)
    print("Robie ciekawe rzeczy w Pythonie")

@dekoruj_cos
def opakowanie_inne():
    print("inna funkcja")

def trzecia_f():
    print("ja tez cos wypisuje")


trzecia_f()
opakowanie_inne()
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


dekorowana('Andrzej')
dekorowana(x="Wojtek")
dekorowana_bez_p()


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

printer("Hello")



# Dodaj dekorator który zliczy czas wykonywania tej funkcji z parametrami. Zaloguj na konsole wszystkie przekazane parametry
def licz_czas_i_loguj(fun):
    def wewnetrzna():
        poczatek = datetime.now()
        fun()
        koniec = datetime.now()
        x = koniec - poczatek
        print(f' wywolanie trwalo {x}')
    return wewnetrzna



def opakuj_mnie_z_parametrami(x, napis_do_wypisania):
    for i in range(x):
        time.sleep(1)
    print(f"Robie ciekawe rzeczy w Pythonie {napis_do_wypisania}")



opakuj_mnie_z_parametrami(3,"jestem cool")
opakuj_mnie_z_parametrami(x=3, napis_do_wypisania="jestem cool")