# A new list is created as a slice of another one containing functions.


def func1():
    return 'uxuam'


def func2():
    return (94, 26, 94)


def func3():
    return {'ekbwl': 61, 'gezdk': 76, 'fokwe': 32}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
