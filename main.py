import random

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