# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return [13, 14, 62]

    return dec


@func1()
def func2():
    return 76.16


a = func2()
