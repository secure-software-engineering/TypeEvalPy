# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return <value1>

    @dec
    def inner():
        return <value2>

    return inner()


a = func()
