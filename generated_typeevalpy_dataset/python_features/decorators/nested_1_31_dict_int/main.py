# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return {'tbdvg': 43, 'mumxp': 54, 'rdigf': 27}

    @dec
    def inner():
        return 71

    return inner()


a = func()
