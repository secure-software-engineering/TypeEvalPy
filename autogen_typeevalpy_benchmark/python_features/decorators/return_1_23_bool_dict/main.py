# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return False

    return dec


@func1()
def func2():
    return {'bkqiw': 71, 'kmsjm': 8, 'depml': 24}


a = func2()
