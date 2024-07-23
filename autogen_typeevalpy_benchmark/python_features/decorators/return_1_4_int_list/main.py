# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 62

    return dec


@func1()
def func2():
    return [42, 3, 29]


a = func2()
