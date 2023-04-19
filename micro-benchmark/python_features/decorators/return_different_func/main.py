# A decorator returns a different function than that assigned to it.


def dec(f):
    def inner():
        f()

    return inner


@dec
def func():
    return "Hello from func"


def func2():
    return func()


a = func2()
