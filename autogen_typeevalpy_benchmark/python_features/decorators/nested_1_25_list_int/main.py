# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return [82, 38, 78]

    @dec
    def inner():
        return 62

    return inner()


a = func()
