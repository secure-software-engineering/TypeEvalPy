# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return {'pxmiy': 30, 'egbii': 7, 'zztve': 13}

    @dec
    def inner():
        return (52, 36, 94)

    return inner()


a = func()
