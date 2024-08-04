# A parameter is passed to a lambda and the lambda calls it.


def func1():
    return {'apqlp': 68, 'csasl': 14, 'yzopf': 73}


def func2():
    return [83, 16, 81]


x = lambda x: x()

a = x(func1)

b = x(func2)
