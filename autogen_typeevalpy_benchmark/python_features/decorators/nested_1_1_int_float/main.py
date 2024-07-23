# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return 51

    @dec
    def inner():
        return 38.57

    return inner()


a = func()
