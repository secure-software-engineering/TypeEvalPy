# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return [49, 56, 64]


def func2():
    return 9.71


ls = [func1, func2]

a = ls[key]()
