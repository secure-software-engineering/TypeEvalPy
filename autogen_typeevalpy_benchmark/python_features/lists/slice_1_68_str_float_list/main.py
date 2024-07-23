# A new list is created as a slice of another one containing functions.


def func1():
    return 'ewjjn'


def func2():
    return 72.5


def func3():
    return [83, 3, 43]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
