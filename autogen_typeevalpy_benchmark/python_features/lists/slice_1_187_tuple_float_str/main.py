# A new list is created as a slice of another one containing functions.


def func1():
    return (76, 35, 80)


def func2():
    return 45.92


def func3():
    return 'vyowc'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
