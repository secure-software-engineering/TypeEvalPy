# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return [52, 40, 54]


def func2():
    return 'wsith'


ls = [func1, func2]

a = ls[key]()
