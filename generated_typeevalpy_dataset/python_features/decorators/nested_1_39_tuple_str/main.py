# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return (7, 9, 23)

    @dec
    def inner():
        return 'jzrje'

    return inner()


a = func()
