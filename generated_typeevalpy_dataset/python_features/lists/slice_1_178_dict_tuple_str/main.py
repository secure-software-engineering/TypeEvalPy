# A new list is created as a slice of another one containing functions.


def func1():
    return {'mtexi': 36, 'szjor': 91, 'nzjmc': 82}


def func2():
    return (93, 77, 81)


def func3():
    return 'oygiz'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
