# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 'mbbjx'

    return dec


@func1()
def func2():
    return 86.74


a = func2()
