# A new list is created as a slice of another one containing functions.


def func1():
    return 79.98


def func2():
    return 'oiwsb'


def func3():
    return (37, 99, 26)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
