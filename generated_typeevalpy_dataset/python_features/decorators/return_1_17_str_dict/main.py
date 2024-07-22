# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 'gvzar'

    return dec


@func1()
def func2():
    return {'hbico': 21, 'htfri': 99, 'sxiku': 22}


a = func2()
