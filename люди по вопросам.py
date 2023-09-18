import xlrd

f = xlrd.open_workbook('answers.xlsx').sheet_by_index(0)
ans = list()
question = list()

for i in range(1):  #список с вопросами
    for j in range(1, 12):
        question.append(f.cell_value(i, j))

for i in range(1, 17):   #создаем список с ответами людей
    name = f.cell_value(i, 0)   #имя
    numbers = ''   #личный код
    for j in range(1, 11):
        numbers += str(int(f.cell_value(i, j)))
    ans += [(numbers, name)]

tek = ''   #текущий код, зависящий от ответов
for x in question:
    print(x)
    if input() in ['Да', 'да']:
        tek += '1'
    else:
        tek += '0'
    i = 0
    while i < len(ans):   #удаление элементов, уже не совпадающих с текущим кодом
        if ans[i][0][:len(tek)] != tek:
            del ans[i]
            i -= 1
        i += 1
    if len(ans) == 1:   #вывести, если остался только один подходящий человек
        print(ans[0][1])
        break
if len(ans) != 1:
    print('Такого человека в группе нет')   #если ответы ни с кем не совпали