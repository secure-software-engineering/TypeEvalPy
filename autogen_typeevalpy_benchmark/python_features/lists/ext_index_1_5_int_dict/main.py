# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return 14


def func2():
    return {'hjbjr': 24, 'srmhe': 22, 'pkfkb': 53}


ls = [func1, func2]

a = ls[key]()
