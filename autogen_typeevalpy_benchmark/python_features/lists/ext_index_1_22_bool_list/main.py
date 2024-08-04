# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return False


def func2():
    return [65, 30, 79]


ls = [func1, func2]

a = ls[key]()
