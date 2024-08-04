# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return [69, 93, 74]


def func2():
    return {'qvtdt': 3, 'mzmix': 21, 'abxbf': 23}


x = lambda x: x()

a = x(func1)

b = x(func2)
