# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return 51


def func2():
    return {'nilgm': 37, 'vcttb': 37, 'hanmq': 94}


ls = [func1, func2]

a = ls[key]()
