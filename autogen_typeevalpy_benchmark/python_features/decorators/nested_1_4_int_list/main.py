# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return 24

    @dec
    def inner():
        return [22, 93, 14]

    return inner()


a = func()
