# A new list is created as a slice of another one containing functions.


def func1():
    return 'nfxkk'


def func2():
    return [20, 54, 27]


def func3():
    return (7, 96, 91)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
