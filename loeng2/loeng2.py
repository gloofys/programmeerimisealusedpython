# sign=input("insert Sign:")
# print(ord(sign))

# uniNumber=int(input("insert Unicode number:"))
# print(chr(uniNumber))

# # Kirjutage programm, mis küsib kasutajalt reaalarvu. Ja kuvaril näitab ümardatud täisarvu.

# realNumber=float(input("insert a real number: "))
# print(round(realNumber))

# arv=int(input("sisesta arv: "))
# aste=int(input("sisesta aste: "))

# outputNumber= pow(arv, aste)
# print(outputNumber)


# arv1=float(input("siesta 1. arv: "))
# arv2=float(input("siesta 2. arv: "))
# arv3=float(input("siesta 3. arv: "))
# arv4=float(input("siesta 4. arv: "))
# arv5=float(input("siesta 5. arv: "))

# miinimumarv=min(arv1, arv2, arv3, arv4, arv5)
# maksimumarv=max(arv1, arv2, arv3, arv4, arv5)

# minrounded=round(miinimumarv, 2)
# maxrounded=round(maksimumarv, 2)

# print(f"miinimumarv on :{minrounded} ja maksimumarv on:{maxrounded}")

import math

R = 6371

phi_1 = 59.4370 # latitude_tallinn
lambda_1 = 24.7536 # longitude_tallinn1
phi_2 = 59.3986 # latidude_kohtla
lambda_2 = 27.2731 #longitude_kohtla


d = 2 * R * math.asin(math.sqrt(math.sin((math.radians(phi_2) - math.radians(phi_1)) / 2)**2 + math.cos(math.radians(phi_1)) * math.cos(math.radians(phi_2)) * math.sin((math.radians(lambda_2) - math.radians(lambda_1)) / 2)**2))

print(round(d, 1))


# Kasutaja sisestab min ja max arvud. Genereeri 3 juhuslikku arvu (min ja max vahemikus) ja leia:

# nende summa
# korrutis
# väikseim ja suurim väärtus

import random

# minarv = int(input("Sisesta min arv: "))
# maxarv = int(input("Sisesta max arv: "))

# juhuslik_1 = random.randint(minarv, maxarv)
# juhuslik_2 = random.randint(minarv, maxarv)
# juhuslik_3 = random.randint(minarv, maxarv)

# print(f"juhuslikud arvud on: {juhuslik_1}, {juhuslik_2}, {juhuslik_3}")

# summa = juhuslik_1 + juhuslik_2 + juhuslik_3
# korrutis = juhuslik_1 * juhuslik_2 * juhuslik_3
# miinimum_arv = min(juhuslik_1, juhuslik_2, juhuslik_3)
# maksimum_arv = max(juhuslik_1, juhuslik_2, juhuslik_3)
# print(f"summa on: {summa}")
# print(f"korrutis on: {korrutis}")
# print(f"miinimum arv on: {miinimum_arv}")
# print(f"maksimum arv on: {maksimum_arv}")

import datetime

birthday = input("insert birthday: (dd.mm.yyyy)")
birthday_converted =  datetime.datetime.strptime(birthday, "%d.%m.%Y")
today = datetime.datetime.now
delta = birthday_converted - today
print(delta.days)
