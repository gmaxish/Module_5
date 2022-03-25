"""
Выведите на экран все числа от 5 до 25 следующим образом:
- Числа кратные 3 и 6 - пропускайте
- для чисел кратных 5, напечатайте строку "N  кратно 5", где N - текущее число
- все остальные числа напечатайте как есть
"""

l = range(5, 26)

for i in l:
    if not i % 3 or not i % 6:
        continue
    print(i, end=" ")
print("")

for i in l:
    if not i % 5 == 0:
        continue
    print(i, "кратно 5")

for i in l:
    if not i % 3 or not i % 6 and not i % 5 == 0:
        print(i, end=" ")