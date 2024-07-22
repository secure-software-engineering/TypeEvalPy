# A parameter is used to index a list.


def func2():
    return {'shduf': 86, 'kskfg': 89, 'htoxy': 10}


def func1(key):
    return ls[key]()


ls = [func1, func2]

a = func1(1)
