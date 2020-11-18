import TestSorts


def choice_sort(arr):
    """Функция сортировки выбором

        бежим по каждой позиции pos в диапазоне от 0 до длины списка - 1 не включительно
        потому что последний элемент списка и так встанет на свое место
        бежим по всем индексам i  в диапазоне начиная с позиции + 1, правее отсортированной части массива,
        до конца
        если тот кто находится в позиции i меньше того кто находится в позиции pos
        то меняем их местами

    """
    for pos in range(0, len(arr) - 1):
        for i in range(pos + 1, len(arr)):
            if arr[i] < arr[pos]:
                arr[i], arr[pos] = arr[pos], arr[i]
    return arr


"""Блок тестов"""
print(TestSorts.test_1(choice_sort))
print(TestSorts.test_2(choice_sort))
print(TestSorts.test_3(choice_sort))
print(TestSorts.test_4(choice_sort))
print(TestSorts.test_5(choice_sort))
print(TestSorts.test_6(choice_sort))
