# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return 89.99


def func2():
    return [13, 70, 68]


ls = [func1, func2]

a = ls[key]()
