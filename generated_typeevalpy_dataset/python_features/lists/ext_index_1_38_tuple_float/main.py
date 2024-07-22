# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return (14, 1, 34)


def func2():
    return 4.59


ls = [func1, func2]

a = ls[key]()
