import random

def generate(start=0, finish=100, quantity=10):
    arr = []
    for _ in range (quantity):
        arr.append(random.randint(start, finish))
    return arr


# Funktsioon genereerib järjendi, mis sisaldab 10 juhuslikku arvu vahemikus 0 kuni 100. Kasuta selleks ülesandes 1 loodud funktsiooni.
# Ekraanile kuvatakse:
# – nende arvude summa,
# – maksimumväärtus,
# – miinimumväärtus.
# Nende näitajate leidmiseks kasuta Pythoni sisseehitatud funktsioone: sum(), max() ja min().
#    Näide:
#    Genireeritud jada: [92, 62, 87, 18, 67, 97, 10, 11, 15, 26]
#    Summa: 
#    Minimaalne arv: 10
#    Maksimaalse arv: 97

def display_sum_max_min():

    arr1 = generate()
    print("Genereeritud jada:", arr1)

    print("Summa:", sum(arr1))
    print("Minimaalne arv:", min(arr1))
    print("Maksimaalne arv:", max(arr1))

display_sum_max_min()

# Funktsioon genereerib järjendi, mis sisaldab 15 juhuslikku arvu vahemikus 0 kuni 50. 
# Sisestage arv klaviatuurilt ja asendage selle arvuga kõik järjendi elemendid, mis on sellest väiksemad.

# def replace_list_elements_from_input():
#     arr2 = generate(0, 50, 15)
#     klava = int(input("sisesta arv"))
#     for i in range(len(arr2)):
#         if arr2[i] < klava:
#             arr2[i] = klava
#     print(arr2)
# replace_list_elements_from_input()

# Funktsioon genereerib järjendi, mis sisaldab 20 juhuslikku arvu vahemikus 0 kuni 150. 
# Ekraanile kuvatakse kõigi paaritute väärtustega elementide indeksid (järjekorranumbrid). Samuti loendatakse, mitu sellist elementi leidus.

def display_uneven_number_indexes_and_count_those_elements():
    arr3 = generate(0, 150, 20)
    count = 0
    for i in range(len(arr3)):
        if arr3[i] % 2 != 0:
            print(i)
            count+= 1
    print ("kokku:", count)
display_uneven_number_indexes_and_count_those_elements()

# Funktsioon genereerib järjendi. Arvutada paarisarvuliste elementide ruutude summa, mis kuuluvad vahemikku [a, b].
def sum_even_squares_in_range(a=0, b=100):
    arr = generate(0, 100, 20)
    print("Genereeritud jada:", arr)

    total = 0

    for x in arr:
        if x % 2 == 0 and a <= x <= b:
            total += x * x   # ruut

    print(f"Ruutude summa paarisarvudel vahemikus [{a}, {b}] on:", total)
sum_even_squares_in_range()