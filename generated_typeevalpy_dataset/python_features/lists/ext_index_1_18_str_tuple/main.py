# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return 'xcnaw'


def func2():
    return (95, 7, 54)


ls = [func1, func2]

a = ls[key]()
