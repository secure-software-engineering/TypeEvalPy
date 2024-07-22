# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return 76.91


def func2():
    return [69, 63, 59]


ls = [func1, func2]

a = ls[key]()
