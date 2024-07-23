# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return 93


def func2():
    return (11, 6, 48)


ls = [func1, func2]

a = ls[key]()
