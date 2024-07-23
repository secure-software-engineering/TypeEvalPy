# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return 'rfxti'

    @dec
    def inner():
        return (92, 26, 67)

    return inner()


a = func()
