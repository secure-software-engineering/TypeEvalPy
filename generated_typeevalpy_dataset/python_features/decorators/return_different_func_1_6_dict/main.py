# A decorator returns a different function than the source function.


def dec(f):
    def inner():
        return {'fypnr': 39, 'baont': 55, 'hhczd': 71}

    return inner


@dec
def func():
    pass


def func2():
    return func()


a = func2()
