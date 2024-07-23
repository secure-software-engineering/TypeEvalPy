# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return {'rcfnk': 62, 'mqmej': 6, 'crrnd': 9}

    return dec


@func1()
def func2():
    return 41


a = func2()
