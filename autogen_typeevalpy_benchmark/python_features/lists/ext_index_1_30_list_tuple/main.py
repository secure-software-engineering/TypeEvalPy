# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return [7, 98, 4]


def func2():
    return (37, 12, 15)


ls = [func1, func2]

a = ls[key]()
