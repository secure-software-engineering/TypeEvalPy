# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return True

    return dec


@func1()
def func2():
    return [47, 2, 55]


a = func2()
