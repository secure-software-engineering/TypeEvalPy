# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return 66.2


def func2():
    return {'cusqq': 10, 'kovpz': 97, 'gmayb': 70}


ls = [func1, func2]

a = ls[key]()
