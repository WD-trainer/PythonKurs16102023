import random

def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    # print_hi('Pyton Kurs')

    tablica = [1,23,43543]
    tab = list()

    tablica.append(2)
    tablica.insert(1, 3432)

    print(f'Element {tablica[0] + tablica[1]}, ostatni element list {tablica[-1]}')

    print(tablica)
    for i in tablica:
        print(i)

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

    print(potegi)
    potegi.append(tablica)
    print(potegi)

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

    # Korzystajac z petli stworz liste zawierajaca elementy same bedace listami. Kazdy taki
    # element ma zawierac numer potegi oraz wartosc tej potegi dla liczby 2.




