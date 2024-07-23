# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 'ezgyf'

    return dec


@func1()
def func2():
    return [21, 93, 10]


a = func2()
