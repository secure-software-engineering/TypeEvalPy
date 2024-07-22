# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return {'bwvnx': 85, 'mugbz': 24, 'mnoln': 40}

    return dec


@func1()
def func2():
    return 1.55


a = func2()
