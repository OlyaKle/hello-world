def insertion_sort(arr): # вспомогательная соритровка, возможна любая, которая проще чем сортировка ведёрками
    for i in range(1, len(arr)):
        cur_el = arr[i]
        while i > 0 and arr[i - 1] > cur_el:
            arr[i] = arr[i - 1]
            i = i - 1
        arr[i] = cur_el

def find_min_max(arr): # вспомогательная функция, для поиска минимума и максимума массива и ускорения работы алгоритма
    if len(arr) == 0:
        return [0, 0] # в случае пустого массива
    min_max = [arr[0], arr[0]]
    for i in arr:
        if i < min_max[0]:
            min_max[0] = i
        if i > min_max[1]:
            min_max[1] = i
    return min_max

def bucket_sort(a, n): # на вход подаются массив и количество блоков(ведёрок)
    buckets = [] # список списков или список блоков
    for i in range(n):
        buckets.append([]) # заполняем список блоков, введённого количества n
    min_max = find_min_max(a) # находим минимум и максимум и создаём из них картеж
    if min_max[0] == min_max[1]: # в случае равенства минимума и максимума массива
        return
    for i in a: # формула распределения каждого элемента относительно заданного количества блоков
        buckets[(n * (i - min_max[0])) // (min_max[1] - min_max[0] + 1)].append(i)
    for bucket in buckets: # в каждом блоке все эелементы исходного массива неотсортированы, но блоки отсортированы относительно друг друга
        if len(bucket) <= 32: # проверка на необходимость делить на блоки каждый блок, если слишком большой блок
            insertion_sort(bucket) # сортировка каждого маленького блока, если они нормальной длины
        else:
            bucket_sort(bucket, n) # рекурсивная сортировка сликшм больших блоков, в последствии каждый из подблоков будет отсортирован выше
    index = 0 # дополнительный индекс, для сборки блоков в общий массив
    for bucket in buckets:
        for i in bucket:
            a[index] = i
            index += 1

if __name__ == '__main__':
     arr = list(map(int, input("Введите эелементы массива через пробел").split()))
     count = int(input("Введите количество ведёрок: "))
     if count < 1:
         print("Невозможное количество ведёрок")
     else:
        bucket_sort(arr, count)
        print(arr)