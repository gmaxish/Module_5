start = 100
finish = 400

while start <= finish:
    x = [int(a) for a in str(start)]
    if int(x[0]) % 2 == 0 and int(x[1]) % 2 == 0 and int(x[2]) % 2 == 0:
        number = ("".join(map(str, x)))
        #print(x)
        print(number)
    start += 1


"""
Выведите на экран все числа в интервале от 100 до 400 включительно, каждое из которых состоят только из четных цифр.
Например 200, 260, 282, 400 и т.д.
"""