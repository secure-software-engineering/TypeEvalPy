# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return [71, 10, 4]

    return dec


@func1()
def func2():
    return 'emsou'


a = func2()
