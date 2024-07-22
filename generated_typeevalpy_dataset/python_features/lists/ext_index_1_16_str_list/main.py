# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return 'oyfov'


def func2():
    return [61, 23, 3]


ls = [func1, func2]

a = ls[key]()
