# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return (18, 68, 35)

    @dec
    def inner():
        return [51, 68, 51]

    return inner()


a = func()
