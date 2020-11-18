def summa(array: list):
    """Сложение элементов массива рекурсией

        сначала из массива достается по одному элементу
        array.pop(len(array) - 1)

        после того как все элементы были вытащены, проихсодит базовый случай

        сейчас summa(array) == базовому случаю, то есть == 0

        теперь вместо этого подставляются значения которые были вытащены и базовый случай
        array.pop(len(array) - 1) + summa(array)

        элемент + 0 --> элмент2 + элемент итд

    """
    if array == []:
        return 0
    return array[0] + sum(array[1:])


def count(array: list):
    """Подсчет элементов в массиве с помощью рекурсии

        1 + counting_of_elements(array[1:])
        при каждом вызове происходит уменьшение массива на 1
        и увеличение глубины рекурсии на 1
        как только дойдет до базового случая, все элементы были подсчитаны
        и мы получаем
        1 + 0 --> 1 + 1 --> 2 + 1 итд == длине массива

    """
    if array == []:
        return 0
    return 1 + count(array[1:])


def top_number(array: list):
    """Нахождение наибольшего числа в списке

        Возвращаем число если оно больше предыдущего

    """
    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]
    sub_max = top_number(array[1:])
    return array[0] if array[0] > sub_max else sub_max


def binary_search(array: list, item: int, start=0, end=None):
    """Бинарный поиск в массиве через рекурсию

        базовый случай: если левая граница больше правой

        сначала рекурсия находит нужный элемент
        потом по цепочки достает его через все вызовы себя же самой

    """
    if end is None:
        end = len(array) - 1
    # Базовый случай
    if len(array) == 1 and array[0] == item:
        return item

    middle = (start + end) // 2
    if item == array[middle]:
        return middle
    elif item < array[middle]:
        # Рекурсивный случай
        return binary_search(array, item, start, middle - 1)
    elif item > array[middle]:
        return binary_search(array, item, middle + 1, end)
    else:
        return None


print(summa([1, 6, 3, 2]))
print(count([6, 2, 1, 6]))
print(top_number([1, 6, 3, 7, 12, 2, 4, 5]))
print(binary_search([x for x in range(1001)], 100))
