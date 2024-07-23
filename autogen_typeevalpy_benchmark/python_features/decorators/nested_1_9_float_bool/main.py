# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return 59.41

    @dec
    def inner():
        return False

    return inner()


a = func()
