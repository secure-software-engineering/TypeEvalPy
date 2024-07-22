# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return 85.54

    @dec
    def inner():
        return [32, 91, 79]

    return inner()


a = func()
