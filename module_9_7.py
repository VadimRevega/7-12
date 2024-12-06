#Цель задания:
#Освоить механизмы создания декораторов Python.
#Практически применить знания, создав функцию декоратор и обернув ею другую функцию.

#Задание:
#Напишите 2 функции:
#Функция, которая складывает 3 числа (sum_three)
#Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.
# ghbvth
#result = sum_three(2, 3, 6)
#print(result)

#Результат консоли:
#Простое
#11

#Примечания:
#Не забудьте написать внутреннюю функцию wrapper в is_prime
#Функция is_prime должна возвращать wrapper
#@is_prime - декоратор для функции sum_three

#Файл module_9_7.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.

# Домашнее задание по теме "Декораторы"

# Функция декоратор (is_prime), которая распечатывает "Простое",
# если результат 1ой функции будет простым числом и "Составное" в противном случае.
def is_prime(func):
# внутренняя функция wrapper в is_prime
    def wrapper(*args, ** kwargs):
        result = func(*args, ** kwargs)
        sum_ = sum(args)
        k = 0
        for i in range(2, sum_ // 2 + 1):
            if sum_ % i == 0:
                k = k +1
        if k <= 0:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper

# @is_prime - декоратор для функции sum_three
@is_prime
# Функция, которая складывает 3 числа (sum_three)
def sum_three(*args):
    return sum(args)



result = sum_three(2, 3, 6)
print(result)
