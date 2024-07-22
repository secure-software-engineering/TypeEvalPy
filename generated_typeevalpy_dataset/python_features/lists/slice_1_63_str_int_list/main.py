# A new list is created as a slice of another one containing functions.


def func1():
    return 'bikxj'


def func2():
    return 31


def func3():
    return [97, 39, 21]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
