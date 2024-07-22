# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return [47, 61, 48]


def func2():
    return {'eheob': 59, 'waifj': 100, 'ptnpl': 36}


ls = [func1, func2]

a = ls[key]()
