# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return 1


def func2():
    return 75.9


ls = [func1, func2]

a = ls[key]()
