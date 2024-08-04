# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return 'ehzjd'


def func2():
    return 34


ls = [func1, func2]

a = ls[key]()
