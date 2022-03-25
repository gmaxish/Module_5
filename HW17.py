"""
Написать программу, которая будет запрашивать у пользователя пароль до тех пор, пока он не удовлетворит следующих
критерий:
- длина пароля не менее 8 символов
- пароль не содердит в себе имя пользователя
"""

name = input("Name: ")
pswd = input("Pswd: ")

while True:
    if len(pswd) < 8:
        print("Too short pswd")
    elif name in pswd:
        print("Pswd contains name")
    else:
        print("Pswd is set")
    pswd = input("Pswd: ")
    break
