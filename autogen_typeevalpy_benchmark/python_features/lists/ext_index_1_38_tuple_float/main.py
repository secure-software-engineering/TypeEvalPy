# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return (8, 91, 99)


def func2():
    return 23.03


ls = [func1, func2]

a = ls[key]()
