# A new list is created as a slice of another one containing functions.


def func1():
    return 52.85


def func2():
    return (38, 37, 25)


def func3():
    return 'wuqay'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
