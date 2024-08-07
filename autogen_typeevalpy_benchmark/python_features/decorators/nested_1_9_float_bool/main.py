# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return 39.3

    @dec
    def inner():
        return True

    return inner()


a = func()
