# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return 24.17


def func2():
    return {'itwfn': 6, 'ogpbg': 30, 'nwexb': 83}


ls = [func1, func2]

a = ls[key]()
