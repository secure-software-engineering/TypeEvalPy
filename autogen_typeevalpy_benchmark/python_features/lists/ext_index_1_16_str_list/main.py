# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return 'mtjtl'


def func2():
    return [63, 77, 88]


ls = [func1, func2]

a = ls[key]()
