# СОРТИРОВКА ВСТАВКАМИ
# Программа получает на вход число n - количество элементов в списке, и затем в следующей
# строке сам список.
# Ваша задача отсортировать список по возрастанию при помощи сортировки вставками,
# в случае если элементы соседние совпадают менять их ненужно.
# В качестве ответа нужно вывести отсортированный список.

n = int(input())
s = list(map(int, input().split()))

for i in range(1, n):
    for j in range(i, 0, -1):
        if s[j] < s[j - 1]:
            s[j], s[j - 1] = s[j - 1], s[j]
        else:
            break
print(*s)