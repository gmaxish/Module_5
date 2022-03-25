"""
Дан список имен ["Rose", "Nina", "Phillip", "Alex", "Jimmy", "Max"]. Вывести на экран приветственное сообщение в
форате "Hello name" для всех имен длиной не более 4х символов. При этом все имена, следующие за именем, содержащие
букву "х", должны быть проигнорированны.
"""

name = ["Rose", "Nina", "Phillip", "Alex", "Jimmy", "Max"]

for i in name:
    if len(i) <= 4:
        print("Hello", i)
        if i.endswith("x"):
            break
            