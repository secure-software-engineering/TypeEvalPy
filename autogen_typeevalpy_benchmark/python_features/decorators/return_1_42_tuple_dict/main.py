# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return (96, 3, 88)

    return dec


@func1()
def func2():
    return {'bgugz': 47, 'shnxk': 65, 'evyei': 71}


a = func2()
