# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return (17, 68, 13)


def func2():
    return 'govix'


ls = [func1, func2]

a = ls[key]()
