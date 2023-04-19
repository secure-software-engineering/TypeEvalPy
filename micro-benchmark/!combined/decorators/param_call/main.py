# The decorator calls the func assigned to it.


def dec(f):
    f()
    return f


@dec
def func():
    a = "In the func"


func()
