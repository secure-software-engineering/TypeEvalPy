# A new list is created as a slice of another one containing functions.


def func1():
    return [20, 9, 89]


def func2():
    return 'gdfir'


def func3():
    return 9


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
