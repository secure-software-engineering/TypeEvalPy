# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return [6, 5, 22]


def func2():
    return (21, 54, 4)


ls = [func1, func2]

a = ls[key]()
