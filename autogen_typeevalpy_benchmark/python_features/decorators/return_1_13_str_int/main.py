# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 'vpjdz'

    return dec


@func1()
def func2():
    return 98


a = func2()
