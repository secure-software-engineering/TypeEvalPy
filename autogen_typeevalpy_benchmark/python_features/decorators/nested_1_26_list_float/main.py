# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return [78, 5, 42]

    @dec
    def inner():
        return 3.43

    return inner()


a = func()
