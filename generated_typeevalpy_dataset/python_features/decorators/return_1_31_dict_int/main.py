# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return {'gqgxd': 21, 'ksqwk': 56, 'fruwv': 34}

    return dec


@func1()
def func2():
    return 22


a = func2()
