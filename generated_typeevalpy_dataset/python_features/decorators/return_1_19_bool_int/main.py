# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return True

    return dec


@func1()
def func2():
    return 100


a = func2()
