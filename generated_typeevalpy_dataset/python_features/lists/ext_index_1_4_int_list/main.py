# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return 19


def func2():
    return [79, 48, 75]


ls = [func1, func2]

a = ls[key]()
