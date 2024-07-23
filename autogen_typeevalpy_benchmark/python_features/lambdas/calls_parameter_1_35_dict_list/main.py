# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return {'expxn': 20, 'gcwkn': 52, 'bowmb': 5}


def func2():
    return [16, 27, 59]


x = lambda x: x()

a = x(func1)

b = x(func2)
