import random

print("GUESS THE NUMBER")

a = int(input("Qaysi sondan boshlanishini yozing: "))
b = int(input("Qaysi songacha bo'lishini yozing: "))

num = random.randrange(a, b + 1)



while True:
    son = int(input("Random sonni toping!"))

    if son > num:
        print("Juda baland")

    elif son < num:
        print("Juda past")

    elif son == num:
        print("To'g'ri topdingiz👏👏👏")
        break