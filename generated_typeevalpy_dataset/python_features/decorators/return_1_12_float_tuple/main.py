# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 62.81

    return dec


@func1()
def func2():
    return (3, 62, 27)


a = func2()
