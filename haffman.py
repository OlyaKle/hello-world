import string # встроенный модуль работы со строками
import re # регулярные выражения
import nltk # библиотека для работы с текстом
from nltk import word_tokenize # модуль для токенизации слов
from nltk.probability import FreqDist # статистика самых частых
from collections import Counter # статистика всех

# import ssl
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
# nltk.download()

if __name__ == '__main__':
    f = open('voyna_i_myr.txt', "r", encoding="utf-8")
    text = f.read()

    text = text.lower() # перевод символов в нижний регистр
    spec_chars = string.punctuation + '«»\t—…’' # добавление к стандартным знакам пунктуации кавычек и многоточий
    text = "".join([ch for ch in text if ch not in spec_chars]) # очистка текста от знаков препинания

    text = re.sub('\n', ' ', text) # замена переносов строк на пробелы
    text = "".join([ch for ch in text if ch not in string.digits]) # удаление из текста цифр

    text_tokens = word_tokenize(text) # токенизация текста
    text = nltk.Text(text_tokens)  # перевод токенов в текстовый формат
    fdist = FreqDist(text) # подсчет слов в тексте по убыванию частоты
    text_counts = Counter(text)
    print(text_counts) # вывод количества вхождений каждого слова
    print(fdist.most_common(5)) # вывод первых 5 самый частых слов