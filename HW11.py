"""
Дано натуральное число N. Определить, является ли оно простым.
"""
N = 17
r = range(2, N)

for j in r:
    if N % j == 0:
        print("Не простое число")
        j += 1
        if True:
            break

    else:
        print("Простое число")
        break
