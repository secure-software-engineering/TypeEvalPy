# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return (8, 96, 90)

    @dec
    def inner():
        return 39

    return inner()


a = func()
