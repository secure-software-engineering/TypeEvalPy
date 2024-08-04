# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 90.73

    return dec


@func1()
def func2():
    return {'dulqz': 5, 'tnlez': 73, 'xesau': 92}


a = func2()
