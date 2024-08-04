# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return (95, 96, 62)


def func2():
    return 'tvytc'


ls = [func1, func2]

a = ls[key]()
