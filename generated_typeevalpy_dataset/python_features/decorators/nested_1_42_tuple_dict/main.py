# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return (100, 65, 67)

    @dec
    def inner():
        return {'lhhns': 40, 'ghwra': 18, 'clsvf': 13}

    return inner()


a = func()
