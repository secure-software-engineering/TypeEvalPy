# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return {'urpqm': 5, 'gyppv': 11, 'wyejp': 2}

    return dec


@func1()
def func2():
    return 18


a = func2()
