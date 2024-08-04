# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return 'hzdps'

    @dec
    def inner():
        return (66, 85, 41)

    return inner()


a = func()
