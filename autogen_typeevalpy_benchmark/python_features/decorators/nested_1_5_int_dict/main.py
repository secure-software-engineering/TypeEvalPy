# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return 58

    @dec
    def inner():
        return {'nvkqt': 15, 'uszyn': 29, 'wtcur': 98}

    return inner()


a = func()
