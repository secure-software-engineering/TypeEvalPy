# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return (10, 39, 66)

    return dec


@func1()
def func2():
    return 36


a = func2()
