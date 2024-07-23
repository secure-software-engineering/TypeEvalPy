# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return (45, 85, 6)


def func2():
    return [79, 42, 80]


ls = [func1, func2]

a = ls[key]()
