# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return False

    @dec
    def inner():
        return (45, 42, 34)

    return inner()


a = func()
