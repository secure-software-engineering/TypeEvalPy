# A new list is created as a slice of another one containing functions.


def func1():
    return (2, 48, 97)


def func2():
    return 49.0


def func3():
    return 'gnwwx'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
