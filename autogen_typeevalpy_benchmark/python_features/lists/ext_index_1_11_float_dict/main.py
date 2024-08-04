# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return 45.9


def func2():
    return {'shjgo': 23, 'stwni': 3, 'qlvzn': 73}


ls = [func1, func2]

a = ls[key]()
