# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return {'bifmm': 71, 'wczan': 69, 'swevx': 93}

    @dec
    def inner():
        return [64, 44, 46]

    return inner()


a = func()
