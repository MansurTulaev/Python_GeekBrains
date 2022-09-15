# 1- Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции

"""Функция принимает на вход массив из чисел.
Далее программа проходит по циклу и считает, является ли индекс нечетным числом.
Если да, то считает сумму элементов"""


def count_odd_sum(array_numbers):
    result: int = 0
    for i in range(len(array_numbers)):
        if i % 2 == 1:
            result += array_numbers[i]
    return result


input_data = [2, 3, 5, 9, 3, 7]
print(count_odd_sum(input_data))

# 2-Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

"""Программа использует алгоритм двух указателей. Первый указатель начинает отсчет индекса элемента с начала,
а второй индекс с конца. Пока первый индекс не станет больше второго, мы умножаем элементы двух индексов"""


def count_multiplication(array_numbers):
    i = 0
    j = len(array_numbers) - 1
    result = []
    while i <= j:
        result.append(array_numbers[i] * array_numbers[j])
        i += 1
        j -= 1
    return result


input_data = [2, 3, 5, 6]
print(count_multiplication(input_data))

# 3-Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов."""

"""Внутри массива происходит расчет дробной части элементов массива.
Затем выводится разница максимального и минимального размера массивов с использованием функций min и max"""


def count_ratio_min_max_sum(array_numbers):
    for i in range(len(array_numbers)):
        array_numbers[i] = array_numbers[i] - int(array_numbers[i])
    array_numbers
    return int((max(array_numbers) - min(array_numbers)) * 100)


input_data = [4.07, 5.1, 8.2444, 6.98]
print(count_ratio_min_max_sum(input_data))

# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное.

"""Записываем в масив остаток от деления на два каждого деления на 2"""


def print_binary(number):
    binary_numbers = []
    while number > 0:
        binary_numbers.append(str(number % 2))
        number = number // 2
    return "".join(binary_numbers[::-1])


print(print_binary(3))


# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

"""Использование цикла для расчета чисел Фибоначчи. Использование функции abs для изменения знака.
Вывод отсортированного массива"""


def print_negative_fib(number):
    fib1 = 1
    fib2 = 1
    i = 0
    result = [fib2, fib1, 0, -abs(fib2), -abs(fib1)]
    while i < number - 2:
        fib_sum = fib1 + fib2
        result.append(fib_sum)
        result.append(-abs(fib_sum))
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    return sorted(result)


print(print_negative_fib(10))
