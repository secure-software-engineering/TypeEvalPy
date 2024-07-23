# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return {'xwehz': 29, 'ugbzg': 88, 'cutml': 99}

    return dec


@func1()
def func2():
    return [2, 82, 97]


a = func2()
