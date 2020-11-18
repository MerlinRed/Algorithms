from repoChoiceSort import TestSorts


def quick_sort(array: list):
    """Быстрая сортировка

        для начала определяется базовый случай
        если в списке содержатся 0 или 1 элемент, то список уже отсортирован
        значит такой нужно вернуть сразу же

        если в списке минимум 2 элемента

        выбирается эталонный(опорный) элемент, с которым будут сравниваться остальные элементы
        определяются массивы которые меньше опорного элемента, равные и больше
        для них вызывается рекурсия, которая делает то же самое,
        после она соединяет меньше эталона + эталон + равный эталону + больше эталона
        и так для всех вызовов рекурсии

        сортировка происходит за O(n log2(n))
        работает не на всех выборках, только до O(n**2)

    """
    if len(array) < 2:
        return array
    support = array[0]
    less = [i for i in array[1:] if i < support]
    greater = [i for i in array[1:] if i > support]
    middle = [i for i in array[1:] if i == support]
    # [support] - потому что конкатинация возможна только если все элементы
    # являются списками, поэтому делаем преобразование
    return quick_sort(less) + [support] + quick_sort(middle) + quick_sort(greater)


"""Блок тестов"""
print(TestSorts.test_1(quick_sort))
print(TestSorts.test_2(quick_sort))
print(TestSorts.test_3(quick_sort))
print(TestSorts.test_4(quick_sort))
print(TestSorts.test_5(quick_sort))
print(TestSorts.test_6(quick_sort))
