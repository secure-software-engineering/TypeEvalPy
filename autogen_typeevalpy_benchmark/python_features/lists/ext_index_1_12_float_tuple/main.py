# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return 71.47


def func2():
    return (27, 79, 92)


ls = [func1, func2]

a = ls[key]()
