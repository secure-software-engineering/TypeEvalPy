# Pass a function as a parameter to a direct call to the return value of a function.


def func():
    return {'jvccj': 90, 'eshfc': 8, 'upnkd': 20}


def func2(a):
    return a


def func3():
    return func2


a = func3()(func)()
