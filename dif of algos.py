import math
# O(3n)
#Что-то делаем с массивом чисел в трех форах
mas=[12,46,6754,34,236,239,613,2111]
print("Исходный массив:", mas)
for i in range(len(mas)):
    mas[i]+=1

for i in range(len(mas)):
    mas[i]=math.sqrt(mas[i])

for i in range(len(mas)):
    if mas[i]%2==0:
        mas[i]+=1

print(mas)

#O(nlog(n))
#сортировка слиянием
def merge_sort(alist, start, end): # функция сортирует список alist от start до end-1 индексов
    if end - start > 1:
        mid = (start + end)//2
        merge_sort(alist, start, mid)
        merge_sort(alist, mid, end)
        merge_list(alist, start, mid, end)

def merge_list(alist, start, mid, end):
    left = alist[start:mid]
    right = alist[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            alist[k] = left[i]
            i = i + 1
        else:
            alist[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            alist[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            alist[k] = right[j]
            j = j + 1
            k = k + 1


alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
merge_sort(alist, 0, len(alist))
print('Sorted list: ', end='')
print(alist)


#O(n!) рекурсия 
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

n=int(input('Введите число: '))
print(f'{n}! =',factorial(n))

#O(n**3) (т.к. три for)
#Задача с прошлой пары: дано n городов, некоторые из них связанные друг с другом дорогами. Найти
#кол-во стран
numc = int(input("Введите количество городов: "))
country = [i for i in range(numc)]
fullm=list()

for i in range(numc):
    s = input(f"Введите {numc} дорог(и), связанных с городом {i+1}: ")
    mas = list(map(int, s.split()))
    fullm.append(mas)
    for j in range(numc):
        if mas[j] == 1:
            for k in range(numc):
                if country[k] == country[j]:
                    country[k] = country[i]

print()
print('Всего стран:', len(set(country)))
print()
print(fullm)

#O(3log(n))
#выполняем бинарный поиск три раза
for i in range(3):
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