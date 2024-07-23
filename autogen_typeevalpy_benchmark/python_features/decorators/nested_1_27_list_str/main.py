# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return [38, 16, 46]

    @dec
    def inner():
        return 'ltoqi'

    return inner()


a = func()
