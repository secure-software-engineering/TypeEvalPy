# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return {'gipim': 50, 'ghfjs': 55, 'gcvyq': 74}


def func2():
    return 21


ls = [func1, func2]

a = ls[key]()
