# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return [52, 48, 64]

    @dec
    def inner():
        return {'gooim': 10, 'ysvpk': 20, 'mqakb': 55}

    return inner()


a = func()
