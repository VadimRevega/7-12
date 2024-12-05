# Домашнее задание по теме "Генераторы"

# Напишите функцию-генератор all_variants(text).
# Пункты задачи: Напишите функцию-генератор all_variants(текст). Опишите логику работы внутри функции all_variants. Вызовите функцию all_variants и выполните итерации. Пример результата выполнения программы: Пример работы функции: a = all_variants("abc"); for i in a: print(i) Вывод на консоль: a b c ab bc abc
# Примечания: Для функции генератора используйте оператор yield.
def all_variants(text):
    # Опишите логику работы внутри функции all_variants.
    for x in range(len(text)):
        for r in range(len(text) - x):
            yield text[x:r + x + 1]


# Вызовите функцию all_variants и выполните итерации.

a = all_variants("abc")
for i in a:
    print(i)