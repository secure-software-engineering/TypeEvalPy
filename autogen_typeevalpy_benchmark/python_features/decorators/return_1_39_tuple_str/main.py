# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return (18, 87, 18)

    return dec


@func1()
def func2():
    return 'ktyrz'


a = func2()
