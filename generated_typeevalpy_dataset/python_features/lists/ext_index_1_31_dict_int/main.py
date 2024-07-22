# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return {'ghsdk': 59, 'hphzt': 37, 'caqkk': 52}


def func2():
    return 10


ls = [func1, func2]

a = ls[key]()
