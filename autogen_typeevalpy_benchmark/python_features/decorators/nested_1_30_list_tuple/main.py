# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return [53, 78, 99]

    @dec
    def inner():
        return (79, 24, 28)

    return inner()


a = func()
