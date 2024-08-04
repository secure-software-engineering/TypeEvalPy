# A new list is created as a slice of another one containing functions.


def func1():
    return 'dvcew'


def func2():
    return (99, 55, 13)


def func3():
    return [98, 83, 58]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
