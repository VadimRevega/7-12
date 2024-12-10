#Цель: понять как работают потоки на практике, решив задачу

#Задача "Потоковая запись в файлы":
#Необходимо создать функцию write_words(word_count, file_name), где word_count - количество записываемых слов, file_name - название файла, куда будут записываться слова.
#Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием после записи каждого на 0.1 секунду.
#Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
#В конце работы функции вывести строку "Завершилась запись в файл <название файла>".



#Пример результата выполнения программы:
#Алгоритм работы кода:
# Импорты необходимых модулей и функций
# Объявление функции write_words
# Взятие текущего времени
# Запуск функций с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы функций
# Взятие текущего времени
# Создание и запуск потоков с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы потоков
#
#Завершилась запись в файл example8.txt
#Завершилась запись в файл example7.txt
#Работа потоков 0:00:20.071575 # Может быть другое время



#Примечания:
#Не переживайте, если программа выполняется долго, учитывая кол-во слов, максимальное время выполнения в потоках не должно превышать ~20 секунд, а в функциях ~34 секунды.
#Cледует заметить, что запись в example8.txt завершилась раньше, чем в example7.txt, т.к. потоки работали почти одновременно.
#Файл module_10_1.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.


from time import sleep
from datetime import datetime
from threading import Thread

time_start = datetime.now()


def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='UTF-8') as file:
        for word in range(1, word_count + 1):
            file.write(f"Какое-то слово № {word} \n")
            sleep(0.1)

    print(f"Завершилась запись в файл {file_name}")
    pass




wite_words(10, "example1.txt")
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

time_and = datetime.now()
time_result = time_and - time_start
print(f'Работа потоков {time_result}')

time_start = datetime.now()

wite_words_1 = Thread(target=wite_words, args=(10, "example5.txt"))
wite_words_2 = Thread(target=wite_words, args=(30, "example6.txt"))
wite_words_3 = Thread(target=wite_words, args=(200, "example7.txt"))
wite_words_4 = Thread(target=wite_words, args=(100, "example8.txt"))

wite_words_1.start()
wite_words_2.start()
wite_words_3.start()
wite_words_4.start()

wite_words_1.join()
wite_words_2.join()
wite_words_3.join()
wite_words_4.join()

time_and = datetime.now()
time_result = time_and - time_start
print(f'Работа потоков {time_result}')