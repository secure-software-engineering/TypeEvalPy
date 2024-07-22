# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return [27, 60, 11]


def func2():
    return 'bpdhm'


ls = [func1, func2]

a = ls[key]()
