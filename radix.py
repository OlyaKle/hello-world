
# получаем цифру, стоящую на текущем разряде в каждом числе массива
def Digit_num(osn, i, j):
    digit = (j // osn ** i) % osn
    return digit

def Counting(maxlen, arr, osn, bins):
    # перебираем все разряды, начиная с нулевого
    for i in range(0, maxlen):
        print(f'Разряд: {str(i)}')
        for j in arr:
            digit = Digit_num(osn, i, j)
            bins[digit].append(j) # отправляем число в промежуточный массив в ячейку, которая совпадает со значением этой цифры
        arr = [x for queue in bins for x in queue] # собираем в исходный массив все ненулевые значения из промежуточного массива
        print(arr)
        print(bins)
        bins = [[] for _ in range(osn)] # очищаем промежуточный массив
    return


def Radix_sort(arr):
    if arr == []:
        return arr
    else:
        # находим размер самого длинного числа
        maxlen = max([len(str(x)) for x in arr])
        osn = 10 # основание системы счисления
        bins = [[] for i in range(osn)] # создаём промежуточный пустой массив из 10 элементов

        Counting(maxlen, arr, osn, bins)
        return arr

if __name__ == '__main__':
    radix_test = [[137137105157, 24395739293, 474290561035, 5, 276, 42], [], [474290561035]]
    for i in radix_test:
        print('-----------New task!!!-----------')
        print(Radix_sort(i))