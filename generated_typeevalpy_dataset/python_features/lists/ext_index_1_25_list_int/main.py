# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return [57, 28, 90]


def func2():
    return 23


ls = [func1, func2]

a = ls[key]()
