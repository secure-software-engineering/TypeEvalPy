# A decorator returns a different function than the source function.


def dec(f):
    def inner():
        return {'tbedu': 50, 'frpui': 35, 'rjfqu': 37}

    return inner


@dec
def func():
    pass


def func2():
    return func()


a = func2()
