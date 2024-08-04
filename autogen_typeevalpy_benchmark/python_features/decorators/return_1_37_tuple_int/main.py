# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return (93, 28, 49)

    return dec


@func1()
def func2():
    return 3


a = func2()
