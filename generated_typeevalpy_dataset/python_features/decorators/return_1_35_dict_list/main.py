# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return {'rnvgy': 98, 'hposc': 51, 'diopk': 34}

    return dec


@func1()
def func2():
    return [73, 59, 21]


a = func2()
