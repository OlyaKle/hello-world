print('Введите элементы массива через пробел: ')
a = list(map(int, input().split()))
num = int(input("Введите искомое число:  "))

a = sorted(a)
res = 0
h = int(len(a) / 2) #половина длины массива
hh = a[h] #средний или средний правый элемент

while num in a:
    if num == hh:
        res += 1
        break
    if num < hh: #меньше среднего -> отрезаем правую
        a = a[:h]
        res += 1
    else: #больше среднего -> отрезаем левую
        a = a[h + 1:]
        res += 1
    h = int(len(a) / 2)
    hh = a[h]

if res == 0:
    print('Числа нет в массиве')
else:
    print('Количество шагов для находения числа: ', res)