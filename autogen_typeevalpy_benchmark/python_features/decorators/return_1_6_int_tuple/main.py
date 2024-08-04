# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 35

    return dec


@func1()
def func2():
    return (79, 54, 9)


a = func2()
