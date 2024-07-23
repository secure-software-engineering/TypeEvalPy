# A new list is created as a slice of another one containing functions.


def func1():
    return 'egiyl'


def func2():
    return [100, 11, 47]


def func3():
    return (27, 91, 64)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
