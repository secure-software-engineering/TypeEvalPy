# A new list is created as a slice of another one containing functions.


def func1():
    return 'toowt'


def func2():
    return 43.07


def func3():
    return False


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
