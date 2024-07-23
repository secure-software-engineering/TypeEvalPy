# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return [21, 13, 55]

    return dec


@func1()
def func2():
    return 75


a = func2()
