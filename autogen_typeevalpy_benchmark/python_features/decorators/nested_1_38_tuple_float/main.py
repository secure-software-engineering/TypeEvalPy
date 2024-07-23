# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return (25, 44, 46)

    @dec
    def inner():
        return 20.64

    return inner()


a = func()
