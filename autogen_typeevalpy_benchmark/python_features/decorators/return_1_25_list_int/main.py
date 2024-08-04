# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return [82, 55, 93]

    return dec


@func1()
def func2():
    return 50


a = func2()
