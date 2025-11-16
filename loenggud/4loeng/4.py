# Testis m'leta et range(5) alusta 0st ja l]peta neljaga ehk 0 , 1 , 2 , 3, 4

# i = 0 
# while i < 5:
#     print("Tere")
#     i += 1


# a = 0
# for a in range(5, 1, -3):
#     print("hello")

# Arva ära number. Kirjutage programm, mis "plaanib" juhusliku arvu vahemikus 1 kuni 10 ja pakub kasutajale ära arvata.
#  Prindib, kas teie arv on suurem või vähem. Printige katsete arv. Kasutage random moodul.

# import random

# comp_number = random.randint(1, 10)
# tries = 1 
# while True:
#     user_number = int(input("arvake number vahemikus 1-10:"))
#     if user_number != comp_number:
#         if user_number > comp_number:
#             print("Arvatav number on v'iksem")
#             tries += 1
#         elif user_number < comp_number:
#             print("Arvatav number on suurem")
#             tries +=1
#     else:
#         print(f"Arvasid oigesti {tries} korraga")


# Siracusa hüpotees ütleb, et mis tahes naturaalarv on taandatav üheks järgmiste toimingute alusel: 
# a) kui arv on paaris, siis jagada see pooleks, 
# b) kui see on paaritu, korrutada 3-ga, lisada 1 ja jagada tulemus kahega. 
# Saadud numbriga korrake samme a) või b) sõltuvalt selle paarsusest. Varem või hiljem arv võrdub ühega.
# Kasutaja sisestab numbri. Printige välja numbrid, mis saadakse toimingute a) ja b) korral. 

# naturaalarv = int(input("sisestage number:"))
# # naturaalarv % 2 == 0:
# while naturaalarv > 1:
#     if naturaalarv % 2 == 0:
#         naturaalarv = naturaalarv / 2 
#         print(f"paaris:{naturaalarv}")
#     elif naturaalarv % 2 != 0:
#         naturaalarv = (naturaalarv * 1 + 1) / 2
#         print(f"paaritu: {naturaalarv}")

# Loo programm, mis simuleerib eksamit, genereerides kasutajale juhuslikke küsimusi. 
# Iga küsimus koosneb kahest juhuslikust arvust ja juhuslikust tehteoperaatorist.

# Programm peab:

# Genereerima 10 küsimust, kus on kaks juhuslikku arvu ja juhuslik tehe (liitmine, lahutamine, korrutamine või jagamine).
# Küsima kasutajalt vastuseid.
# Loendama õigete vastuste arvu.
# Kui õigeid vastuseid on rohkem kui 7, kuvama teate: "Eksami tulemus: sooritatud", vastasel juhul: "Eksami tulemus: mitte sooritatud".
# Vihje: Kasuta random.randint juhuslike arvude genereerimiseks ja random.choice tehteoperaatori valimiseks. 
# random.choice("+-*/")   # juhuslik märk otse stringist

# import random
# import operator


# oiged_vastused = 0 
# kusimused = 1

# while kusimused <= 10:
#     juhuslik1 = random.randint(1, 10)
#     juhuslik2 = random.randint(1, 10)

#     juh_tehe = random.choice("+-*/")
#     print(f"{juhuslik1} {juh_tehe} {juhuslik2}")
#     if juh_tehe == "+":
#         tehte_vastus = operator.add(juhuslik1, juhuslik2)
#     elif juh_tehe == "-":
#         tehte_vastus = operator.sub(juhuslik1, juhuslik2)
#     elif juh_tehe == "*":
#         tehte_vastus = operator.mul(juhuslik1, juhuslik2)
#     elif juh_tehe == "/":
#         tehte_vastus = operator.floordiv(juhuslik1, juhuslik2)
#     print(f"{tehte_vastus}")
    
#     kusimused += 1
#     vastus = int(input("Sisesta vastus:"))
#     if tehte_vastus == vastus:
#         oiged_vastused += 1

# if oiged_vastused > 7:
#     print("Eksami tulemus: sooritatud")
# else:
#     print("Eksami tulemus: mittesooritatud")

# Ristkülik
# Looge programm, mis joonistab ristküliku (pesastatud tsükli abil). Küljete pikkused määrab kasutaja. Ristküliku saab joonistada  * abil. Näiteks:
# *    *    *    *    *
# *    *    *    *    *
# *    *    *    *    *


# korgus = int(input("sisesta korgus:"))
# laius = int(input("sisesta laius:"))

# for i in range(korgus):
#     for j in range(laius):
#         print(f"* ", end="")
#     print()

# Püramiidi kontuur
# Antud kood, mis prindib püramiidi. Kuidas muuta koodi nii, et prindib ainult selle püramiidi kontuur ja kõigi sisemiste märkide asemel on tühikud?
         
for i in range(6):
    for j in range(i+1):
        print("*", end="")
    print()