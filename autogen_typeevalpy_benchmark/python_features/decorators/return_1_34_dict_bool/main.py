# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return {'eymat': 19, 'pgmxv': 13, 'dzfhg': 95}

    return dec


@func1()
def func2():
    return True


a = func2()
