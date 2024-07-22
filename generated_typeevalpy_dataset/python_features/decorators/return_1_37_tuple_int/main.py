# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return (55, 56, 19)

    return dec


@func1()
def func2():
    return 18


a = func2()
