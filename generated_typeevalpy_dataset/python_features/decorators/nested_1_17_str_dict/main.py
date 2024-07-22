# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return 'tkwah'

    @dec
    def inner():
        return {'wichn': 44, 'ehuoa': 62, 'efvdk': 31}

    return inner()


a = func()
