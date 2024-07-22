# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return [54, 83, 52]

    @dec
    def inner():
        return 'shald'

    return inner()


a = func()
