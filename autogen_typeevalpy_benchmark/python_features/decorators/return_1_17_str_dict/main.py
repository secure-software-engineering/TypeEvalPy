# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 'qlkio'

    return dec


@func1()
def func2():
    return {'revfc': 94, 'xkgzc': 10, 'fwvbc': 91}


a = func2()
