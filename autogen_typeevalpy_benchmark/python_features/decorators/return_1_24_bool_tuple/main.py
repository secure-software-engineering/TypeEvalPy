# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return False

    return dec


@func1()
def func2():
    return (40, 11, 55)


a = func2()
