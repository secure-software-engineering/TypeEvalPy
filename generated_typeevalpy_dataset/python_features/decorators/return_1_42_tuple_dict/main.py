# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return (59, 49, 90)

    return dec


@func1()
def func2():
    return {'pdbef': 69, 'eiqls': 48, 'cleqg': 95}


a = func2()
