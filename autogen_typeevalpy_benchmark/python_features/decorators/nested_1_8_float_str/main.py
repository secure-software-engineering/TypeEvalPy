# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return 76.27

    @dec
    def inner():
        return 'qqaxf'

    return inner()


a = func()
