# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 47

    return dec


@func1()
def func2():
    return {'kibdd': 49, 'nupjl': 96, 'ayzqh': 21}


a = func2()
