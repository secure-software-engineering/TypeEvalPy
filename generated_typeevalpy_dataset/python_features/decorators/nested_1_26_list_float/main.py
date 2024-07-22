# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return [57, 73, 90]

    @dec
    def inner():
        return 39.47

    return inner()


a = func()
