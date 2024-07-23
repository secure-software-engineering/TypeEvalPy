# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 'hmoxs'

    return dec


@func1()
def func2():
    return (36, 50, 26)


a = func2()
