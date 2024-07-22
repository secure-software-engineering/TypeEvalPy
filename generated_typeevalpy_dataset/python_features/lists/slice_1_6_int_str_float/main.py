# A new list is created as a slice of another one containing functions.


def func1():
    return 54


def func2():
    return 'odhyg'


def func3():
    return 91.84


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
