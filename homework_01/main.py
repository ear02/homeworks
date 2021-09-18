"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*nums):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    res = []
    for n in nums:
        res.append(n ** 2)
    return res

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    # если число не делится без остатка на что-либо кроме 1
    # и само не равно 1, то добавляем его в результат
    result = True
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            result = False
            break
    return result


def filter_numbers(nums, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    # для получения нечётных проверяем, чтобы остаток от деления на 2 был не равен 0
    if filter_type == 'odd':
        return list(filter(lambda num: num % 2 != 0, nums))
    # для получения чётных проверяем, чтобы остаток от деления на 2 был равен 0
    if filter_type == 'even':
        return list(filter(lambda num: num % 2 == 0, nums))
    # число простое, если делится только на себя и 1
    # проверяем каждый элемент списка циклом от 2 до элемента
    if filter_type == 'prime':
        res = []
        for n in nums:
            if is_prime(n):
                res.append(n)
        return res


# # проверка
# # квадраты
# print(power_numbers(1, 2, 5, 7))
# # нечётные
# print(filter_numbers([1, 2, 3], ODD))
# # чётные
# print(filter_numbers([2, 3, 4, 5], EVEN))
# # простые
# print(filter_numbers([1, 2, 3, 4, 5, 6, 7], PRIME))
