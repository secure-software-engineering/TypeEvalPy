# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 10

    return dec


@func1()
def func2():
    return {'aqqgy': 90, 'bghpc': 66, 'nswnj': 68}


a = func2()
