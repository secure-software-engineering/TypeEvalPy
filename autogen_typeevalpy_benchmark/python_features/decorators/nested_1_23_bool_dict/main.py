# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return True

    @dec
    def inner():
        return {'zezkq': 86, 'brczg': 69, 'fesyo': 68}

    return inner()


a = func()