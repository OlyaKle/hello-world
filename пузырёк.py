def bubble_sort(a):
    temp = 0
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
    return(a)
if __name__ == '__main__':
    a = []
    a = list(map(int, input("Введите эелементы массива через пробел").split()))
    ans = bubble_sort(a)
    print("Отсортированный массив:", ans)

