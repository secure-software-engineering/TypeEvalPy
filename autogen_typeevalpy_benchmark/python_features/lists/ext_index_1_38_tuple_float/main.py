# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return (46, 50, 8)


def func2():
    return 42.33


ls = [func1, func2]

a = ls[key]()
