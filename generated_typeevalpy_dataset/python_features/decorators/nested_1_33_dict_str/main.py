# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return {'dmrjn': 79, 'nkpxs': 51, 'zklxt': 85}

    @dec
    def inner():
        return 'kclen'

    return inner()


a = func()
