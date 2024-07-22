# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return {'memvy': 13, 'xhkat': 60, 'svxog': 56}


def func2():
    return (72, 58, 43)


ls = [func1, func2]

a = ls[key]()
