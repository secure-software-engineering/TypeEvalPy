# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 86.44

    return dec


@func1()
def func2():
    return 20


a = func2()
