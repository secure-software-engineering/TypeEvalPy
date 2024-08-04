# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return (81, 18, 78)

    @dec
    def inner():
        return 96.0

    return inner()


a = func()
