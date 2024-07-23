# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return {'xmtof': 33, 'vibjd': 32, 'hfbfb': 94}


def func2():
    return [44, 100, 68]


ls = [func1, func2]

a = ls[key]()
