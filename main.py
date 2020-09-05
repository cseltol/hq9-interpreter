f = open(input('Enter file name: ')) # Ввод осуществляется из файла
s = f.read()                         # Вывод на консоль
f.close()                            # Для простоты, любые другие символы мы будем просто игнорировать

template = '''{} bottles of beer on the wall.
Take one down and pass it around, {} bottles of beer on the wall.'''

count = 0                            # Никому не нужный счётчик

for i in s.upper():                  # Игнорируем регистр

    if i == 'H':
        print('Hello, world!')       # Выводим 'Hello, world!'

    elif i == 'Q':
        print(s)                     # Выводим саму программу

    elif i == '9':

        for i in range(99, 1, -1):
            print(template.format(i, i-1))  # Выводим текст песни
        print('1 bottle of beer on the wall.\nTake one down and pass it around, no more bottles of beer on the wall.')
        print('No more bottles of beer on the wall.\nGo to the store and buy some more, 99 bottles of beer on the wall.')

    elif i == '+':
        count += 1