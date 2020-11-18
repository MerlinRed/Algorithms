def test_1(alghorithm):
    array = [3, 4, 2, 1, 6, 7, 8, 5, 5, 5, 5, 5, 3, 3, 3, 3, 2, 2, 2, 4, 4]
    sorted_array = alghorithm(array)
    array = [3, 4, 2, 1, 6, 7, 8, 5, 5, 5, 5, 5, 3, 3, 3, 3, 2, 2, 2, 4, 4]
    check_array = sorted(array)
    if sorted_array == check_array:
        return 'TestCase#1: Ok'
    else:
        return 'TestCase#1: Fail'


def test_2(alghorithm):
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    sorted_array = alghorithm(array)
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    if sorted_array == array:
        return 'TestCase#2: Ok'
    else:
        return 'TestCase#2: Fail'


def test_3(alghorithm):
    array = []
    sorted_array = alghorithm(array)
    if sorted_array == array:
        return 'TestCase#3: Ok'
    else:
        return 'TestCase#3: Fail'


def test_4(alghorithm):
    array = [-1, -2, -3, -4, 0, 1, 2, 3, 4]
    sorted_array = alghorithm(array)
    array = [-1, -2, -3, -4, 0, 1, 2, 3, 4]
    check_array = sorted(array)
    if sorted_array == check_array:
        return 'TestCase#4: Ok'
    else:
        return 'TestCase#4: Fail'


def test_5(alghorithm):
    array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    sorted_array = alghorithm(array)
    array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    check_array = sorted(array)
    if sorted_array == check_array:
        return 'TestCase#5: Ok'
    else:
        return 'TestCase#5: Fail'


def test_6(alghorithm):
    array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    sorted_array = alghorithm(array)
    array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    check_array = sorted(array)
    if sorted_array == check_array:
        return 'TestCase#6: Ok'
    else:
        return 'TestCase#6: Fail'


if __name__ == '__main__':
    test_1(alghorithm)
    test_2(alghorithm)
    test_3(alghorithm)
    test_4(alghorithm)
    test_5(alghorithm)
    test_6(alghorithm)
