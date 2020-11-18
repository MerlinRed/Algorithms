def binary_search(array, item):
    """Бинарный поиск в массиве

        берем левую крайнюю и правую крайнюю границы массива
        пока левая граница меньше или равна правой делаем следующее
        бьем в середину массива, чтобы сократить диапазон поиска
        если елемент находится в левой части от середины
        тогда середина становится правой границей - 1, потому что середина не является тем что мы ищем,
        она проверена
        если элемент находится в правой части от середины, тогда середина это левая граница -1
        если в массиве не оказалось элемента, возвращаем None
        скорость выполнения алгоритма O(log2(n))

    """
    left_border = 0
    right_border = len(array) - 1  # так как left_border добавляет 1 элемент
    while left_border <= right_border:
        middle = (left_border + right_border) // 2  # чтобы указать на точный элемент
        if item == array[middle]:
            return middle
        elif item < right_border:
            right_border = middle - 1
        elif item > left_border:
            left_border = middle + 1
        else:
            return None


"""Блок тестов"""


def test_1():
    array = [x for x in range(101)]
    search_element = binary_search(array, 100)
    if search_element == 100:
        return 'TestCase#1: Ok'
    else:
        return 'TestCase#1: Fail'


def test_2():
    array = []
    search_element = binary_search(array, 0)
    if search_element == 0:
        return 'TestCase#2: Fail'
    else:
        return 'TestCase#2: Ok'


print(test_1())
print(test_2())
