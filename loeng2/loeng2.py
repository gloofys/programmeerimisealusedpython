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


arv1=float(input("siesta 1. arv: "))
arv2=float(input("siesta 2. arv: "))
arv3=float(input("siesta 3. arv: "))
arv4=float(input("siesta 4. arv: "))
arv5=float(input("siesta 5. arv: "))

miinimumarv=min(arv1, arv2, arv3, arv4, arv5)
maksimumarv=max(arv1, arv2, arv3, arv4, arv5)

minrounded=round(miinimumarv, 2)
maxrounded=round(maksimumarv, 2)

print(f"miinimumarv on :{minrounded} ja maksimumarv on:{maxrounded}")