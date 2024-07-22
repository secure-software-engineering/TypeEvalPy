# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return [79, 2, 39]

    @dec
    def inner():
        return 30

    return inner()


a = func()