# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return 41

    @dec
    def inner():
        return (26, 84, 62)

    return inner()


a = func()
