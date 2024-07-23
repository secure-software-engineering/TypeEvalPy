# A new list is created as a slice of another one containing functions.


def func1():
    return 18.12


def func2():
    return True


def func3():
    return 'yoshl'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
