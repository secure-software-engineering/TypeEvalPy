# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return {'xrvbu': 87, 'fczju': 86, 'kxblq': 52}

    @dec
    def inner():
        return 'tbdmf'

    return inner()


a = func()
