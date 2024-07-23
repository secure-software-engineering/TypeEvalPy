# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return (76, 28, 43)

    return dec


@func1()
def func2():
    return 3.86


a = func2()
