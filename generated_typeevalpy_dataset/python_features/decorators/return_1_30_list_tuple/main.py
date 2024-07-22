# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return [68, 54, 39]

    return dec


@func1()
def func2():
    return (18, 49, 14)


a = func2()
