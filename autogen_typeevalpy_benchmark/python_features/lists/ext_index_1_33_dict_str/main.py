# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return {'ndcpo': 27, 'xcmol': 74, 'zaunu': 53}


def func2():
    return 'czvfp'


ls = [func1, func2]

a = ls[key]()
