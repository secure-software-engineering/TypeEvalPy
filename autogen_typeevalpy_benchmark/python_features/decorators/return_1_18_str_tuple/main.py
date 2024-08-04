# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 'guuax'

    return dec


@func1()
def func2():
    return (77, 7, 39)


a = func2()
