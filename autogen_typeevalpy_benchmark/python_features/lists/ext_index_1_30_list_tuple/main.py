# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return [23, 16, 86]


def func2():
    return (78, 64, 1)


ls = [func1, func2]

a = ls[key]()
