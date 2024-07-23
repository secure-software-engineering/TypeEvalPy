# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return [1, 54, 30]

    return dec


@func1()
def func2():
    return 28.43


a = func2()
