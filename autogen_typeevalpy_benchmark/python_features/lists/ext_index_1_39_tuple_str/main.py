# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return (65, 84, 16)


def func2():
    return 'acvdf'


ls = [func1, func2]

a = ls[key]()
