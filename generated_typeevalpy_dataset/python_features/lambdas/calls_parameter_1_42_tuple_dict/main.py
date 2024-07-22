# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return (95, 13, 29)


def func2():
    return {'rdfsz': 34, 'hzrij': 23, 'bzjox': 78}


x = lambda x: x()

a = x(func1)

b = x(func2)
