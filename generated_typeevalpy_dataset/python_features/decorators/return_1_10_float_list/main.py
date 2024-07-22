# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 64.06

    return dec


@func1()
def func2():
    return [80, 16, 3]


a = func2()
