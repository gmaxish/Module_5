"""
Вычислить сумму натуральных четных чисел, не превышающих N.
"""

n = 100
s = 0

for i in range(0, n + 1):
    if i%2 == 0:
        print(i)
        s += i
print(s)
