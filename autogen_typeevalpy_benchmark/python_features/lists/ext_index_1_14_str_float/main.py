# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return 'wunpm'


def func2():
    return 16.98


ls = [func1, func2]

a = ls[key]()
