# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return (68, 8, 48)

    return dec


@func1()
def func2():
    return 35.85


a = func2()
