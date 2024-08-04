# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 'ufldr'

    return dec


@func1()
def func2():
    return 7.5


a = func2()
