# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return (47, 82, 74)


def func2():
    return {'vsvsd': 70, 'qzadf': 80, 'ugtdf': 87}


ls = [func1, func2]

a = ls[key]()
