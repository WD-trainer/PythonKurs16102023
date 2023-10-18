import pytest

from day3 import sumuj, dajCyfry


def test_sumuj():
    assert sumuj(5,3) == 10

def test_dajCyfryMin():
    tab=dajCyfry()
    assert min(tab) == 1

def test_dajCyfryMax():
    tab=dajCyfry()
    assert max(tab) == 10

def test_dajCyfryLen():
    tab=dajCyfry()
    assert len(tab) == 10


# Stworz w osobnym module funkcje ktora bedzie zwracala liste 100 losowych liczb z zakresu 1-100.
# Dodaj testy jednostkowe ktory beda sprawdzaly czy funkcja zwrocila 100 elementow,
# czy wszystkie mieszcza sie w zakresie 1-100 i czy wszystkie zwracane wartosci sa liczbami calkowitymi
