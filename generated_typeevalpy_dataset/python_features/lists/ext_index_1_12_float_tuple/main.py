# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return 47.12


def func2():
    return (62, 16, 46)


ls = [func1, func2]

a = ls[key]()
