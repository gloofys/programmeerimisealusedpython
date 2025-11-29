##range i (2)
## range(3, 4, ´-1) vastus 0
## x = 21 y=14 hile x!y if x>y x=x-y, else y = y-x, vastus x=7 y = 7

# import operator

# def arithmetic():
#     number_1 = int(input("Sisesta 1. number: "))
#     number_2 = int(input("Sisesta 2. number: "))
#     user_operator = input("Sisesta operaator (+, -, *, /): ")

#     if user_operator == "+":
#         return operator.add(number_1, number_2)
#     elif user_operator == "-":
#         return operator.sub(number_1, number_2)
#     elif user_operator == "*":
#         return operator.mul(number_1, number_2)
#     elif user_operator == "/":
#         return operator.truediv(number_1, number_2)
#     else:
#         return "Tundmatu operatsioon"

# print(arithmetic())

# def power():
#     result = 1

#     while True:
#         number = int(input("Sisesta number: "))
#         if number == 0:
#             break
#         result *= number
#     return result

# print(power())

def calculate_discount():
    price = int(input("Sisesta algne hind"))
    discount = int(input("sisesta allahindlus"))

    if discount < 100 :
        hind = (discount * 0,1) * price
        return hind
    else : "return tundmatu protsent"
print(calculate_discount())