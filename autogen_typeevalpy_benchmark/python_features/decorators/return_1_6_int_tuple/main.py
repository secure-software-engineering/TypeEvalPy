# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 93

    return dec


@func1()
def func2():
    return (31, 18, 56)


a = func2()
