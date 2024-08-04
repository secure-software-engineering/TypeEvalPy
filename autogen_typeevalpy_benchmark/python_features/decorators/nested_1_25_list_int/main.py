# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return [26, 69, 86]

    @dec
    def inner():
        return 97

    return inner()


a = func()
