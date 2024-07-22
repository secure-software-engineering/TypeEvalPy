# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return False

    return dec


@func1()
def func2():
    return {'guuye': 97, 'qxsks': 31, 'hvsaj': 54}


a = func2()
