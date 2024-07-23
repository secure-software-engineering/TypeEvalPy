# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 'dyotc'

    return dec


@func1()
def func2():
    return {'iguer': 3, 'jiowk': 72, 'qnvsg': 91}


a = func2()
