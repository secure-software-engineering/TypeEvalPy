# A new list is created as a slice of another one containing functions.


def func1():
    return (26, 21, 51)


def func2():
    return {'ruopn': 2, 'uiszu': 63, 'msefb': 6}


def func3():
    return 63.34


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
