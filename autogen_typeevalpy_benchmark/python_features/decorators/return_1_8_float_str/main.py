# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 60.9

    return dec


@func1()
def func2():
    return 'yfnto'


a = func2()
