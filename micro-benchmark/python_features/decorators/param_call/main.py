# The decorator calls the func assigned to it.


def dec(f):
    a = f()
    return a


@dec
def func():
    a = "In the func"
    return a


b = func()
