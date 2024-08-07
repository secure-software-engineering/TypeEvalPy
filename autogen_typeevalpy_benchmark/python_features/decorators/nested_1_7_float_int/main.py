# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return 20.05

    @dec
    def inner():
        return 54

    return inner()


a = func()
