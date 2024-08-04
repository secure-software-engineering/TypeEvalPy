# A new list is created as a slice of another one containing functions.


def func1():
    return [94, 13, 45]


def func2():
    return 21.77


def func3():
    return 'bnahe'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
