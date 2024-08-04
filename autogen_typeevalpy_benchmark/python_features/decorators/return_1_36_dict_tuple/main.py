# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return {'phmre': 21, 'jjjle': 81, 'etltw': 82}

    return dec


@func1()
def func2():
    return (47, 65, 60)


a = func2()
