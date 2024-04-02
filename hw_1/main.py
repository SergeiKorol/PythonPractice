
# Первое задание
def power_numbers(numbers:list[int]) -> list[int]:
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел

    """
    # использую новые знания list comprehension
    return(list([num*num for num in numbers]))

numbers = [1, 2, 5, 7]

print(power_numbers(numbers))


# Второе задание

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"
PPP = "qwe"

#Для начала проверим является ли число num простым
def is_prime(num:int)-> bool:
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_numbers(filter_numbers:list[int], filter_type:str)-> list[int| None]:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    """

    if filter_type == ODD:
        return list(filter(lambda x: x % 2 != 0, numbers))
    elif filter_type == EVEN:
        return list(filter(lambda x: x % 2 == 0, numbers))
    elif filter_type == PRIME:
        return list(filter(is_prime, numbers))
    else:
        print("Неправильный тип фильтра. Используйте 'odd', 'even' или 'prime'.")
        return []


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(filter_numbers(numbers, ODD))
print(filter_numbers(numbers, EVEN))
print(filter_numbers(numbers, PRIME))
print(filter_numbers(numbers, PPP))