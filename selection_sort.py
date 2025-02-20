# Сортировка выбором

n = int(input())
a = list(map(int, input().split()))
for i in range(n-1):
    m = a[i] #min значение
    p = i #индекс мин значения
    for j in range(i + 1, n):
        if m > a[j]:
            m = a[j]
            p = j
        if p != i:
            t = a[i]
            a[i] = a[p]
            a[p] = t
print(a)

