# A new list is created as a slice of another one containing functions.


def func1():
    return [61, 20, 83]


def func2():
    return 75.36


def func3():
    return 'rfrtp'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
