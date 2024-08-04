# A new list is created as a slice of another one containing functions.


def func1():
    return 'wffyu'


def func2():
    return 83.92


def func3():
    return (36, 32, 81)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
