# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 49

    return dec


@func1()
def func2():
    return 12.03


a = func2()
