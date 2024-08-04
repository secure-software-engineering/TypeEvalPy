# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return [53, 37, 50]

    @dec
    def inner():
        return (82, 5, 75)

    return inner()


a = func()
