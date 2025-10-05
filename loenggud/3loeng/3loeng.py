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

piletinr = int(input("sisesta 6-kohaline piletikood:"))

piletNr1 = (piletinr // 100000) % 10
piletNr2 = (piletinr // 10000) % 10
piletNr3 = (piletinr // 1000) %10
piletNr4 = (piletinr // 100) % 10
piletNr5 = (piletinr // 10) % 10
piletNr6 = piletinr % 10

if piletNr1 + piletNr2 + piletNr3 == piletNr4 + piletNr5 + piletNr6:
    print("teie pilet on õnnelik")
else:
    print("pilet pole õnnelik")