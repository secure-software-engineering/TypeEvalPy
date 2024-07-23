# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return 12.6

    @dec
    def inner():
        return (81, 29, 47)

    return inner()


a = func()
