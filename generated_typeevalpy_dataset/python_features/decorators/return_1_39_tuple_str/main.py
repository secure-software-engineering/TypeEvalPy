# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return (83, 58, 67)

    return dec


@func1()
def func2():
    return 'bazlx'


a = func2()
