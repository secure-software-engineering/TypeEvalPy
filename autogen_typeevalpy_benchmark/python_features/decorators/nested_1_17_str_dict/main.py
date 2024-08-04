# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return 'gfcze'

    @dec
    def inner():
        return {'fujwm': 43, 'laiax': 57, 'nskxt': 58}

    return inner()


a = func()
