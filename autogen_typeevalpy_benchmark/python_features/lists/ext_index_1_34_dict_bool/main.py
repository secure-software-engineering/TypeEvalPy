# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return {'pbyyx': 16, 'tbetc': 76, 'qcjca': 72}


def func2():
    return False


ls = [func1, func2]

a = ls[key]()
