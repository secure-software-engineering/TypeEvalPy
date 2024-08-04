# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return (87, 59, 68)

    @dec
    def inner():
        return [55, 64, 89]

    return inner()


a = func()
