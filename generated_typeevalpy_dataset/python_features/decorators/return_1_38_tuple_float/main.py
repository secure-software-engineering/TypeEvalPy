# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return (91, 65, 39)

    return dec


@func1()
def func2():
    return 9.64


a = func2()
