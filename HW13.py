"""
Дана последовательность целых чисел. Найти наименьшее положительное число среди элементов последовательности.
Если присутствует несколько одинаковых наименьших элементов, то определеить их количество.
"""
le = [4, -1, 5, 7, 3, 11, 15, 2, 11, 51, 2, 2]
min = le[0]
K = []

for i in range(1, len(le)):
    if le[i] < min and le[i] > 0:
        min = le[i]
print(min)
print(le.count(min))