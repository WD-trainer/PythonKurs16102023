
import Moduly_i_pakiety.pakiet as p

p.hello()


# zaimportuj 2 funkcje z modulu pakiet2 (na 3 rózne sposoby) - (sayyes, sayno) i wywował je
import Moduly_i_pakiety.pakiet2 as p2
from Moduly_i_pakiety.pakiet2 import sayyes

p2.sayno()
sayyes()


# wywołaj funkcje add - dodaj do niej dokumentacje, i wypisz ta dokumentacje na konsoli
from Moduly_i_pakiety.pakiet2 import add

help(add)

print(add(2,2))


from MojeFunkcje import funkcje
from MojeFunkcje import SesjaDB

import MojeFunkcje as mf

mf.odejmowanie(2,2)

print(SesjaDB)

funkcje.hello_world()


# stworzyli pakiet wypisywacz który będize zawiereał __init__.py - print z informacjami o pakiecie + import
# stworzy plik z pisacz, w nim napisz hello world i zaimportuj i wywołaj
from wypisywacz import pisanie

if __name__ == "__main__":
    pisanie()

