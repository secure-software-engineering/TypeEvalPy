# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 74

    return dec


@func1()
def func2():
    return {'bdlvq': 7, 'rllfp': 71, 'zkayk': 60}


a = func2()
