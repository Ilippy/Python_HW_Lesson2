# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# a + b = x
# a * b = y
# Ввод:
# 7
# 12
# Вывод
# 3 4 или 4 3
def printList(l):
    if l:
        for a, b in l:
            print(a, b)
    else:
        print(f"Для x = {x} и y = {y} не было найдено значений a и b")


x, y = int(input("Введите значение x\n")), int(input("Введите значение y\n"))
size = x + 1 if x > y else y + 1

# 1й способ
# array = []
# for a in range(size):
#     for b in range(size):
#         if a + b == x and a * b == y:
#             #print(a, b)
#             array.append((a, b))
# printList(array)

# 2й способ
# a = [(a, b) for a in range(size) for b in range(size) if a+b==x and a*b==y]
# printList(a)

# 3й способ (самый быстрый)
array = set()
if y == 0:
    array.add((0, x))
    array.add((x, 0))
else:
    for a in range(1, size//2):
        b = x - a
        if  a * b == y:
            array.add((b, a))
            array.add((a, b))
printList(array)
