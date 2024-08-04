# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return (96, 4, 100)

    return dec


@func1()
def func2():
    return {'fhcxh': 57, 'ymijs': 76, 'nrfmg': 76}


a = func2()
