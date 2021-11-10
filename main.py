'''Шифр "Вставка в середину". Дан текст. Осуществить шифрование и дешифрование следующим образом:
текст разбивается на группы из четного количества элементов, в каждой группе символы переставляются некоторым образом
(например, записываются в обратном порядке) и в середину добавляются n случайных символов, далее переставляются сами группы символов
При использовании шифра «Вставка в середину» сначала необходимо разделить открытый текст СЕКРЕТНОЕ СООБЩЕНИЕ на группы букв так,
чтобы в каждой группе было четное количество букв. В результате получим:
'''

import random

group_size = 6 #должен быть четным
n = 1 #столько слчайных символов будет добавлено в каждую группу
fill = chr(0) #не должен быть равен одному из символов текста

text = 'Секрет'

def text_encode(text, group_size, n, fill):
    groups = []
    separator = int(group_size / 2)

    #если текст английский, то в rnd1 должны быть английские буквы
   #rnd1 = 'abcdefghijklmnopqrstuvwxyz'
    rnd1 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    rnd2 = rnd1.upper()
    rnd3 = '0123456789 .,?!-:'
    rndChars = rnd1 + rnd2 + rnd3

    #разбиение на группы
    for i in range(0, len(text), group_size):
        groups.append(text[i:i+group_size])
    #к последней группе добавляется заполнитель
    groups[-1] += fill * (group_size - len(groups[-1]))
    #символы в каждой группе записываются в обратном порядке
    #и в середину добавляется n случайных символов
    for index, group in enumerate(groups):
        rnd = ''.join(random.choices(rndChars, k=n))
        temp = group[::-1]

        groups[index] = temp[:separator] + rnd + temp[separator:]
    #группы переставляются в обратном порядке
    groups = groups[::-1]

    return ''.join(groups)

def text_decode(text, group_size, n, fill):
    groups = []
    separator = int(group_size / 2)

    #разбиение на группы
    for i in range(0, len(text), group_size+n):
        temp = text[i:i+group_size+n][::-1] #инверсия группы
        group = temp[:separator] + temp[separator+n:]
        groups.append(group)
    #группы переставляются в обратном порядке
    groups = groups[::-1]

    return ''.join(groups).replace(fill, '')

encode = text_encode(text, group_size, n ,fill)
print('Зашифрованый текст:')
print(encode)

decode = text_decode(encode, group_size, n ,fill)
print('\nРасшифрованый текст:')
print(decode)