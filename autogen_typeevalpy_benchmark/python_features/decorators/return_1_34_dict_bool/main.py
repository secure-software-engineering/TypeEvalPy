# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return {'xhjom': 82, 'apqhc': 18, 'loqax': 16}

    return dec


@func1()
def func2():
    return False


a = func2()
