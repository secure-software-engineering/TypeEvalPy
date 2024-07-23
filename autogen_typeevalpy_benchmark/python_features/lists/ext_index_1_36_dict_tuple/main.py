# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return {'rhjab': 17, 'byxsu': 96, 'hpuwt': 70}


def func2():
    return (12, 33, 8)


ls = [func1, func2]

a = ls[key]()
