# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 'tudcc'

    return dec


@func1()
def func2():
    return 13.62


a = func2()
