# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return [36, 1, 60]

    return dec


@func1()
def func2():
    return 'sntku'


a = func2()
