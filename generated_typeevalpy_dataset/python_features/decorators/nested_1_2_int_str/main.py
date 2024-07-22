# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return 38

    @dec
    def inner():
        return 'exauz'

    return inner()


a = func()
