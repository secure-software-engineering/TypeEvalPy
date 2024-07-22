# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return 83


def func2():
    return {'gbtts': 54, 'grarf': 2, 'tdfzx': 63}


ls = [func1, func2]

a = ls[key]()
