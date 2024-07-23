# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return {'ddbph': 23, 'vlsxw': 28, 'pouhb': 39}

    return dec


@func1()
def func2():
    return 99.63


a = func2()
