
def merge_sort(alist, start, end): # функция получает на фход массив, счетчик нулевого и счетчик последнего элемента
    if end - start > 1: # 1 и 0 элементов не полдежат сортировке
        mid = (start + end) // 2 # округление в меньшую сторону
        merge_sort(alist, start, mid) # получится отсортированная первая половина элементов и неотсортированнная правая
        merge_sort(alist, mid, end) # получатся две остортированные половины, неотсортированные между собой
        merge_list(alist, start, mid, end) # функция слияния/смерживания двух полумассовов


def merge_list(alist, start, mid, end): # получает на вход мас, счетчик начала, конца и середины
    left = alist[start:mid] # создадим массив для левой отсортированной половины
    right = alist[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            alist[k] = left[i] # после сравнения первых двух, запишем меньший(левый) в изначальный массив(алист) вместо первого
            i = i + 1 # перейдем на следующий элемент в массиве из которого взяли меньший
        else:
            alist[k] = right[j] # аналогично, если меньший оказался в правом массиве
            j = j + 1
        k = k + 1
    if start + i < mid: # если какой-то из массивов(правый/левый) закончился:
        while k < end: # закончился правый
            alist[k] = left[i]
            i = i + 1
            k = k + 1
    else: # закончился левый
        while k < end: # запишем все оставшиеся элементы из незакончившегося массива
            alist[k] = right[j]
            j = j + 1
            k = k + 1

if __name__ == '__main__':
    alist = input('Enter the list of numbers: ').split()
    alist = [int(x) for x in alist]
    merge_sort(alist, 0, len(alist))
    print('Sorted list: ', alist)
