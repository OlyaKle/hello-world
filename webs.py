import asyncio
import webbrowser
import re

# карутины, которые принимают запрос или ссылку и открывают его в браузере
async def open_web_one(call):
    await asyncio.sleep(3)
    if re.search(r'\.', call):
        webbrowser.open_new_tab('https://' + call) # проверка на ввод или вызов internet explorer
        print(f'Результат поиска: {call} в браузере')
    elif re.search(r'\ ', call):
        webbrowser.open_new_tab('https://www.google.com/search?q={}'.format(f'{call}'))
        print(f'Результат поиска: {call} в браузере')
    else:
        webbrowser.open_new_tab('https://www.google.com/search?q={}'.format(f'{call}'))
        print(f'Результат поиска: {call} в браузере')

async def open_web_two(call):
    await asyncio.sleep(2)
    if re.search(r'\.', call):
        webbrowser.open_new_tab('https://' + call)  # проверка на ввод или вызов internet explorer
        print(f'Результат поиска: {call} в браузере')
    elif re.search(r'\ ', call):
        webbrowser.open_new_tab('https://www.google.com/search?q={}'.format(f'{call}'))
        print(f'Результат поиска: {call} в браузере')
    else:
        webbrowser.open_new_tab('https://www.google.com/search?q={}'.format(f'{call}'))
        print(f'Результат поиска: {call} в браузере')

async def open_web_three(call):
    await asyncio.sleep(1)
    if re.search(r'\.', call):
        webbrowser.open_new_tab('https://' + call)  # проверка на ввод или вызов internet explorer
        print(f'Результат поиска: {call} в браузере')
    elif re.search(r'\ ', call):
        webbrowser.open_new_tab('https://www.google.com/search?q={}'.format(f'{call}'))
        print(f'Результат поиска: {call} в браузере')
    else:
        webbrowser.open_new_tab('https://www.google.com/search?q={}'.format(f'{call}'))
        print(f'Результат поиска: {call} в браузере')


async def main():
    one_call = input('Введите первую ссылку или запрос: ')
    two_call = input('Введите вторую ссылку или запрос: ')
    thr_call = input('Введите вторую ссылку или запрос: ')
    task1 = asyncio.ensure_future(open_web_one(f'{one_call}'))
    task2 = asyncio.ensure_future(open_web_two(f'{two_call}'))
    task3 = asyncio.ensure_future(open_web_three(f'{thr_call}'))

    await asyncio.gather(task1, task2, task3)

asyncio.run(main())

# # новый цикл обработки событий
# loop = asyncio.get_event_loop()
# # запуск карутина в цикле обработки событий
# loop.run_until_complete(main())
# # закрытие цикла обработки событий
# loop.close()

# webbrowser.open_new_tab('https://www.google.com/search?q=%D1%81%D0%BC%D0%B0%D0%B9%D0%BB%D0%B8%D0%BA+%D1%83%D1%80%D0%B0&oq=%D1%81%D0%BC%D0%B0%D0%B9%D0%BB%D0%B8%D0%BA+%D1%83%D1%80%D0%B0&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDINCAQQLhivARjHARiABDIICAUQABgWGB6oAgCwAgA&sourceid=chrome&ie=UTF-8')
# webbrowser.open_new_tab('https://www.google.com/search?q={}'.format(f'{call}'))









