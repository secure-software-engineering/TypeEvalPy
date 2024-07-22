# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return 99.34

    @dec
    def inner():
        return {'iusqt': 30, 'zncyz': 71, 'mxdzt': 77}

    return inner()


a = func()
