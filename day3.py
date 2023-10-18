import random
def sumuj(a,b):
    return a+b

def dajCyfry():
    return list(range(1,11))

def losowa_lista():
    return [random.randint(1,100) for i in range(100)]




podpietaBaza=None
def podepnijBaze(nazwa):
    global podpietaBaza
    podpietaBaza=nazwa
def wykonajZapytanie():
    global podpietaBaza
    print('Wykonuję zapytanie z użyciem bazy{}'.format(podpietaBaza))
    if(podpietaBaza=='MS SQL'):
        raise Exception('FUUUUUUU')
    return "ok"



baza=[]
def loadDB():
    print("############## ŁADOWANIE BAZY ##############")
    global baza
    baza=[
    (1,"Marian"),
    (2,"Czesław"),
    (3,"Zenon"),
    (4,"Florian")
    ]

def getData():
    global baza
    return baza
def getOne(x):
    global baza
    return baza[x]


def nieprzetestowana_funckja(a):
    if a > 10:
        print(f"Hahahahaha a mnie nie przetestowałeś! {a}")
    print(f"Testing")


import requests

def fetch_data():
    response = requests.get("https://example.com/api/data")
    return response.text



# https://joblib.readthedocs.io/en/stable/parallel.html

# https://refactoring.guru/pl/design-patterns

# https://www.lucidchart.com/pages/pl/czym-jest-uml-unified-modeling-language

# https://www.w3schools.com/python/python_regex.asp#sub
# https://regex101.com/
