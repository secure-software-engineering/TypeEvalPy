# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 'hhuts'

    return dec


@func1()
def func2():
    return 51


a = func2()
