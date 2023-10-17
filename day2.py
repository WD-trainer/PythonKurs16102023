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


def opakuj_mnie():
    time.sleep(3)
    print("Robie ciekawe rzeczy w Pythonie")

