# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return {'ubpax': 5, 'cbckv': 7, 'piiis': 13}

    @dec
    def inner():
        return 61

    return inner()


a = func()
