# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 79

    return dec


@func1()
def func2():
    return 96.38


a = func2()
