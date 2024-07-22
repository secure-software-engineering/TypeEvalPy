# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return 61

    @dec
    def inner():
        return (7, 92, 34)

    return inner()


a = func()
