# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return 70

    @dec
    def inner():
        return 67.53

    return inner()


a = func()
