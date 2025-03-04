
import os # У этого модуля есть функция, которая показывает содержимое папки по указанному пути - os.listdir(path)

path = 'C:\\Movies'  # храниться путь к нашей корневой папке


def scan_dir(path, level=1):
    print('Level=', level, 'Content:', os.listdir(path)) # показывает содержимое папки по указанному пути - содержимое
                                                         # получим в виде списка, значит его можно обойти при помощи
                                                         # цикла for
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i): # path.isdir - определяет, является ли элемент файлом или папкой
                                           # os.path.isfile - Проверка на то, является ли документ файлом или нет
                                           # for i in os.listdir(path):
                                           #     print(path + '\\' + i, os.path.isfile(path + '\\' + i))
            print('Спускаемся', path + '\\' + i)
            scan_dir(path + '\\' + i, level + 1)
            print('Возвращаемся в', path)


scan_dir(path)

#Теперь краткое объяснение его работы: в самом начале вызываем функцию и передаём ей адрес Movies. Потом выводится
# содержимое этой папки и затем все эти элементы мы начинаем обходить в цикле for. Первый элемент – hello.txt, который
# не является папкой, поэтому он пропускается. Джанго освобожденный является каталогом, поэтому мы вновь рекурсивно
# вызываем нашу функцию и попадаем в эту папку, выводится содержимое этой папки и, если там есть ещё папки, то рекурсивно
# продолжается вхождение в папку. И так до тех пор, пока в каталоге не будет других папок, после этого идёт сообщение,
# что мы возвращаемся в предыдущую папку и, если есть другие папки внутри неё, то спускаемся туда, если нет – возвращаемся
# в предшествующую папку. И так до тех пор, пока все папки не будут пройдены.