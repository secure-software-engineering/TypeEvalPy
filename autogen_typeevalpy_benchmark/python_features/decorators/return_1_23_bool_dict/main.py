# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return False

    return dec


@func1()
def func2():
    return {'oxzsz': 55, 'qrlvp': 67, 'anzyb': 10}


a = func2()
