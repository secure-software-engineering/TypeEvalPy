# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return False


def func2():
    return {'ztsek': 89, 'lchfp': 73, 'vafzy': 16}


ls = [func1, func2]

a = ls[key]()
