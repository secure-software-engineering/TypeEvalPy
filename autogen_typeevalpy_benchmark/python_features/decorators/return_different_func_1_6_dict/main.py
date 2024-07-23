# A decorator returns a different function than the source function.


def dec(f):
    def inner():
        return {'fsrkb': 7, 'paohz': 5, 'rynxi': 84}

    return inner


@dec
def func():
    pass


def func2():
    return func()


a = func2()
