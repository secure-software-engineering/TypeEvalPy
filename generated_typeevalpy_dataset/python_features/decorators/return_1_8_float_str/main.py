# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 39.21

    return dec


@func1()
def func2():
    return 'dzzht'


a = func2()
