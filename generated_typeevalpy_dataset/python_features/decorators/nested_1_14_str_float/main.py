# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return 'dpfok'

    @dec
    def inner():
        return 93.59

    return inner()


a = func()
