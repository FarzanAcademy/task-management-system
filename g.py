import random

bat=random.randint(10,100)
hp=8
b=1
while b <= hp:
    user=int(input("hads: "))
    if user == bat:
        print("bordi🎉")
        break
    elif user < bat:
        print("bozorg")
    elif user > bat:
        print("kochak")
    b = b + 1

if user != bat:
    print("game over🤣🤣")
    print(bat)