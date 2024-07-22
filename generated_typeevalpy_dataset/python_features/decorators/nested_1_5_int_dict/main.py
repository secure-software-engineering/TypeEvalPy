# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return 72

    @dec
    def inner():
        return {'fxvfg': 34, 'vnjbe': 2, 'issqi': 10}

    return inner()


a = func()
