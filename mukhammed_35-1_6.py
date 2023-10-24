from random import randint

a = []
for i in range(10):
    a.append(randint(1, 10))
a.sort()
print(a)

value = int(input())

mid = len(a) // 2
low = 0
high = len(a) - 1


while a[mid] != value and low <= high:
    if value > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("Элемент не найден")
else:
    print("Индекс элемента =", mid)
