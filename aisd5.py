def thief(a, n, m, k):
    itog = ([], 0)
    sum_i = 0  # количество унесённых элементов
    cur_m = 0  # текущее количество заходов
    cur_mm = 0  # текущее количество заходов
    max_sum = 0  # текущая сумма унесённых элементов
    maximum = 0  # максимальная сумма, за счет которой мы определим конечный массив весов
    res = []  # экспонаты, которые вор смог унести
    ch = 0
    for i in a:
        if i <= k:
            if sum_i < n and cur_m < m:
                res.append(i)
                cur_m += 1
                sum_i += 1
                max_sum += i
        elif i > k:
            if sum_i < n and cur_m < m:
                while ch < i and cur_mm < (m - cur_m):
                    ch += k
                    cur_mm += 1
                if i - ch == 0:
                    sum_i += 1
                    cur_m += cur_mm
                    res.append(i)
                    max_sum += i
                cur_mm = 0
                ch = 0
    if max_sum > maximum:
        maximum = max(maximum, max_sum)
        itog = (res, maximum)
    return (itog)


if __name__ == '__main__':
    a = list(map(int, input("Введите эелементы массива через пробел:").split()))
    a = sorted(a)
    n = int(input("Введите число экспонатов, которые хочет унести вор:"))
    m = int(input("Введите число заходов, которые должен сделать вор:"))
    k = int(input("Введите максимальный вес, который вор уносит за 1 заход:"))
    res = thief(a, n, m, k)
    if res == ([], 0):
        print("Вор не осуществит задумку")
    else:
        print(f"Вору выгоднее унести следующие элементы: {res[0]}, максимальная сумма вынесенных элементов: {res[1]}")

# check:
# a = [8, 4, 6, 9]
# n = 1
# m = 1
# k = 3