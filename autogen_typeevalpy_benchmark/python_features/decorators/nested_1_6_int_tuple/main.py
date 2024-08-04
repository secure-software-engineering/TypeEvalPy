# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return 6

    @dec
    def inner():
        return (35, 69, 32)

    return inner()


a = func()
