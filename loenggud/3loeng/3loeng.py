# taisarv=int(input("sisesta täisarv"))
# print(f"{taisarv} on paaris {taisarv % 2 == 0}")


# number1 = int(input("sisesta esimene arv:"))
# number2 = int(input("sisesta teine arv:"))

# print(number1==number2)


# number3 = int(input("sisesta arv:"))




# distance1InKm = int(input("sisesta esimene distants(km):"))
# distance2InFt = int(input("sisesta teine distants(ft):"))
# ftToKm = 0.0003048
# # ft=0,3048m = 0,0003048km

# distance2InKm = distance2InFt * ftToKm

# if distance1InKm > distance2InKm:
#     print("distants 1 on suurem")
# elif distance1InKm < distance2InKm:
#     print("distance 2 on suurem")
# else:
#     print("distantsid on v]rdsed")


# kknumber= int(input("Sisesta kahekohaline number:"))

# kknumber1 = (kknumber // 10) % 10
# kknumber2 = kknumber % 10


# if kknumber1 > kknumber2:
#     print("1 number on suurem")
# elif kknumber1 < kknumber2:
#     print("2 number on suurem")
# else:
#     print("numbrid on v]rdsed")

# if (kknumber1+kknumber2) / 10 < 1 :
#     print("arvude summa on ühekohaline number")
# else:
#     print("arvude summa on kahekohaline")

# if kknumber1 / 3 == 1 or kknumber2 / 3 ==1 :
#     print("arv sisaldab numbrit 3")
# else:
#     print("arv ei sisalda numbrit 3")


# nadalapaev = int(input("Sisesta nädalapäeva number (1-7):"))


# match nadalapaev:
#     case 1:
#         print("1 - see on esmaspäev")
#     case 2:
#         print("2 - see on teisipäev")
#     case 3:
#         print("3 - see on kolmapäev")
#     case 4:
#         print("4 - see on neljapäev")
#     case 5:
#         print("5 - see on reede")
#     case 6:
#         print("6 - see on laupäev")
#     case 7:
#         print("7 - see on pühapäev")
    

# 4. Pilet
# Ühistranspordis saadud pilet (kasutaja sisestab) loetakse õnnelikuks, kui  kuuekohalise numbri korral langeb esimese kolme numbri summa kokku kolme viimase numbri summaga.

# piletinr = int(input("sisesta 6-kohaline piletikood:"))

# piletNr1 = (piletinr // 100000) % 10
# piletNr2 = (piletinr // 10000) % 10
# piletNr3 = (piletinr // 1000) %10
# piletNr4 = (piletinr // 100) % 10
# piletNr5 = (piletinr // 10) % 10
# piletNr6 = piletinr % 10

# if piletNr1 + piletNr2 + piletNr3 == piletNr4 + piletNr5 + piletNr6:
#     print("teie pilet on õnnelik")
# else:
#     print("pilet pole õnnelik")

#     5. Matemaatiliste operatsioonide test
# Kirjuta programm, mis genereerib viis juhuslikku matemaatikaülesannet, kus kasutaja peab:

# Korrutama kaks juhuslikku arvu.
# Liitma kaks juhuslikku arvu.
# Lahutama ühe juhusliku arvu teisest.
# Jagama täisarvuliselt ühe juhusliku arvu teisega.
# Leiutama ühe arvu jagamisel teisega jäägi (modulo operatsioon).
# Matemaatikaülesanded:
import random

score = 0

exercise1number1 = random.randint(1,10)
exercise1number2 = random.randint(1,10)
exercise1 = exercise1number1 * exercise1number2
print(f"mis on {exercise1number1} * {exercise1number2}?")
answer1 = int(input("Teie vastus:"))
if exercise1 == answer1:
    print("teie vastus on oige")
    score += 1 
else:
    print(f"teie vastus on vale, õige vastus on {exercise1}")


exercise2number1 = random.randint(1,10)
exercise2number2 = random.randint(1,10)
exercise2 = exercise2number1 + exercise2number2
print(f"mis on {exercise2number1} + {exercise2number2}?")
answer2 = int(input("Teie vastus:"))
if exercise2 == answer2:
    print("teie vastus on oige")
    score += 1 
else:
    print(f"teie vastus on vale, õige vastus on {exercise2}") 


exercise3number1 = random.randint(1,10)
exercise3number2 = random.randint(1,10)
exercise3 = exercise3number1 - exercise3number2
print(f"mis on {exercise3number1} - {exercise3number2}?")
answer3 = int(input("Teie vastus:"))
if exercise3 == answer3:
    print("teie vastus on oige")
    score += 1 
else:
    print(f"teie vastus on vale, õige vastus on {exercise3}") 



exercise4number1 = random.randint(1,10)
exercise4number2 = random.randint(1,10)
exercise4 = exercise4number1 // exercise4number2
print(f"mis on {exercise4number1} : {exercise4number2} täisarvuline jagamine?")
answer4 = int(input("Teie vastus:"))
if exercise4 == answer4:
    print("teie vastus on oige")
    score += 1 
else:
    print(f"teie vastus on vale, õige vastus on {exercise4}") 

exercise5number1 = random.randint(1,10)
exercise5number2 = random.randint(1,10)
exercise5 = exercise5number1 % exercise5number2
print(f"mis on {exercise5number1} : {exercise5number2} jagamise jääk?")
answer5 = int(input("Teie vastus:"))
if exercise5 == answer5:
    print("teie vastus on oige")
    score += 1 
else:
    print(f"teie vastus on vale, õige vastus on {exercise5}") 


print(f"Teie tulemus: {score} õiget vastust 5-st.")
