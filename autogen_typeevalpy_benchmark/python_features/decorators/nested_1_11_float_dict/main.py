# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return 67.07

    @dec
    def inner():
        return {'zdwys': 59, 'qglne': 36, 'sfoio': 85}

    return inner()


a = func()
