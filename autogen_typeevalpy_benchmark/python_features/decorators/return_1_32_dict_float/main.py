# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return {'wvggq': 23, 'ddxmt': 31, 'bihrk': 79}

    return dec


@func1()
def func2():
    return 66.21


a = func2()
