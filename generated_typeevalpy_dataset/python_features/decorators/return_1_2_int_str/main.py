# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 16

    return dec


@func1()
def func2():
    return 'xzmff'


a = func2()
