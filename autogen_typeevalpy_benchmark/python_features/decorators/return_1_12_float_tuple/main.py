# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 44.59

    return dec


@func1()
def func2():
    return (42, 33, 63)


a = func2()
