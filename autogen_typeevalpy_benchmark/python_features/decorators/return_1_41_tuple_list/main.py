# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return (11, 48, 26)

    return dec


@func1()
def func2():
    return [18, 82, 58]


a = func2()
