import pytest

from day3 import sumuj, dajCyfry, losowa_lista, loadDB,getOne,getData, fetch_data, nieprzetestowana_funckja


def test_sumuj():
    assert sumuj(5,3) == 8

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
def test_losowLista_Len():
    tab=losowa_lista()
    assert len(tab) == 100

def test_losowLista_wartosci():
    tab=losowa_lista()
    for i in tab:
        assert i <= 100 and i >= 1

def test_losowLista_typ():
    tab = losowa_lista()
    for i in tab:
        assert isinstance(i, int)


import day3
# def test_podepnijBaze():
#     bazy=['Oracle','PostgreSQL','MS SQL','MySQL']
#     for b in bazy:
#         day3.podepnijBaze(b)
#     assert day3.wykonajZapytanie() == 'ok'
#     pass

# dbs = ["Oracle", 'PostgreSQL', 'MS SQL', 'MySQL']
# @pytest.mark.parametrize('baza', dbs)
# def test_podepnijBaze(baza):
#     day3.podepnijBaze(baza)
#     print('{}\n'.format(baza))
#     assert day3.wykonajZapytanie()=='ok'

def setup_module():
    print("\n############## setup ##############")
    loadDB()
def teardown_module():
    print("\n############## bye ##############")
def test_getData():
    assert len( getData() )>0

def test_getOne():
    assert getOne(0)[1]=='Marian'


import unittest.mock

def test_fetch_data():
    mock_response = unittest.mock.MagicMock()
    mock_response.text = "Test data"

    with unittest.mock.patch('requests.get', return_value=mock_response):
        result = fetch_data()

    assert result == "Test data"

def test_prosty():
    nieprzetestowana_funckja(6)
    assert True