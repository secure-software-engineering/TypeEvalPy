# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return True


def func2():
    return 61.13


ls = [func1, func2]

a = ls[key]()