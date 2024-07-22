# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return {'oyogo': 90, 'eoghm': 44, 'uzmmd': 4}

    return dec


@func1()
def func2():
    return False


a = func2()
