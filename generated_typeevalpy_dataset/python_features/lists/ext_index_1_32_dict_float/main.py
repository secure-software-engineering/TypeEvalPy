# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return {'zkcly': 1, 'itqfw': 99, 'dhmbm': 20}


def func2():
    return 54.0


ls = [func1, func2]

a = ls[key]()
