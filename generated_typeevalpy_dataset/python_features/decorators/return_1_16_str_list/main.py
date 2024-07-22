# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 'lqgfv'

    return dec


@func1()
def func2():
    return [47, 8, 54]


a = func2()
