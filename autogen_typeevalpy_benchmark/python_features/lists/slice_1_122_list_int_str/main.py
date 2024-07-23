# A new list is created as a slice of another one containing functions.


def func1():
    return [85, 70, 48]


def func2():
    return 67


def func3():
    return 'dpjdr'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
