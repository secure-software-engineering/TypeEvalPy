# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return {'qwjil': 54, 'kdkbf': 66, 'hyzda': 24}


def func2():
    return [21, 65, 59]


ls = [func1, func2]

a = ls[key]()
