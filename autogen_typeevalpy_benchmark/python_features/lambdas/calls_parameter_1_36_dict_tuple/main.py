# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return {'oovrh': 42, 'dgrpr': 67, 'ahjcw': 98}


def func2():
    return (51, 28, 58)


x = lambda x: x()

a = x(func1)

b = x(func2)
