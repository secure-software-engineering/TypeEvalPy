# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 56.88

    return dec


@func1()
def func2():
    return [35, 72, 40]


a = func2()
