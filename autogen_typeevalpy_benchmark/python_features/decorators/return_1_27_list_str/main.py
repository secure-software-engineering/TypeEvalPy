# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return [88, 20, 78]

    return dec


@func1()
def func2():
    return 'hzkwb'


a = func2()
