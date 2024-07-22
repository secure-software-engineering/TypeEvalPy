# A new list is created as a slice of another one containing functions.


def func1():
    return (59, 13, 82)


def func2():
    return 'pwbny'


def func3():
    return [16, 12, 7]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
