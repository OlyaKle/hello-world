# создаём класс, как шаблон объекта 'стек', который будет инициализировать команды pop, push
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item): # теперь push добавлет в конец массива
        self.stack.append(item)
    def pop(self): # теперь pop удаляет с конца массива
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed

def lifo(a): # функция, кот принимает на вход строку
    cur_s = a # вспомогательная строка для сохранности исходной
    s = Stack() # преобразуем строку в стек
    l = len(cur_s)
    for i in range(len(cur_s)):
        if l != 0 and cur_s[i] == '(':
            s.push('(')
            l -= 1
            brokeni = 0 # в случае правильного массива вернёт нулевой индекс, который выводиться не будет
        elif l != 0 and s.stack == [] and cur_s[i] == ')':
            s.push(')')
            l -= 1
            brokeni = i # в случае неправильного массива вернёт индекс с которого нет парных скобок
            break
        elif l != 0 and cur_s[i] == ')':
            s.pop()
            l -= 1
            brokeni = 0 # в случае правильного массива вернёт нулевой индекс, который выводиться не будет
    return (s.stack, brokeni) # возвращаем пустой стек или непарные скобки и индекс с которого сломалось

global brokeni # глобальная переменная для того самого индекса, с которого всё ломается

if __name__ == '__main__':
    brokeni = 0
    structure = input("Print your structure")
    res = lifo(structure)
    if res[0] == []:
        print(f'Structure {structure} is true')
    else:
        print(f'Structure {structure} is wrong, index broken item', res[1])
