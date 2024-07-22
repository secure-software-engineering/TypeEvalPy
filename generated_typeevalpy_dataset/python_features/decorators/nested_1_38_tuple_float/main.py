# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return (73, 23, 21)

    @dec
    def inner():
        return 80.09

    return inner()


a = func()
