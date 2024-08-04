# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 'xehvi'

    return dec


@func1()
def func2():
    return [78, 83, 16]


a = func2()
