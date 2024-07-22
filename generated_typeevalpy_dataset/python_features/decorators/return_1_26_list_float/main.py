# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return [62, 97, 29]

    return dec


@func1()
def func2():
    return 45.44


a = func2()
