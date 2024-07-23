# A new list is created as a slice of another one containing functions.


def func1():
    return 'vgdkr'


def func2():
    return (71, 65, 35)


def func3():
    return 55


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
