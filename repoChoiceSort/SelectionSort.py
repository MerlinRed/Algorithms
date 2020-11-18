import TestSorts

"""Рекурсивная сортировка выбором"""


def find_smallest(arr):
    """Функция по нахождению наименьшего значения из массива

        предполагаем, что самый наименьший это первый элемент из массива
        создаем переменную, куда добавим найденный наименьший элемент
        бежим по списку в диапазоне от 1 до конца длины массива
        проверяем каждый индекс в массиве, если он меньше эталонного индекса
        тогда ставим его эталоном и добавляем в переменную, и так далее пока не найдем наименьший

    """
    smallest = arr[0]
    smallest_element = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_element = i
    return smallest_element


def selection_sort(arr):
    """Функция сортировки выбором

        создаем переменную  для пустого списка(массив), который вернем с отсортированными элементами
        бежим по длине списка
        делаем вызов функции по нахождению наименьшего значения из массива
        добавляем в переменную элемент который нашла вызванная функция

    """
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


"""Блок тестов"""
print(TestSorts.test_1(selection_sort))
print(TestSorts.test_2(selection_sort))
print(TestSorts.test_3(selection_sort))
print(TestSorts.test_4(selection_sort))
print(TestSorts.test_5(selection_sort))
print(TestSorts.test_6(selection_sort))
