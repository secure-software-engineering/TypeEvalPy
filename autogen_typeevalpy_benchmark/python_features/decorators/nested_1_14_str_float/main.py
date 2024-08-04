# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return 'zcuio'

    @dec
    def inner():
        return 64.02

    return inner()


a = func()
