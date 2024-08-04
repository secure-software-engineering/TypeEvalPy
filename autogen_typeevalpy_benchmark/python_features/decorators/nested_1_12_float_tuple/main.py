# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return 77.82

    @dec
    def inner():
        return (91, 31, 57)

    return inner()


a = func()
