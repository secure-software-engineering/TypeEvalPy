# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 99

    return dec


@func1()
def func2():
    return (83, 54, 52)


a = func2()
