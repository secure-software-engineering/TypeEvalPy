# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return 86

    @dec
    def inner():
        return {'puzlf': 59, 'bbfoa': 71, 'owxgx': 74}

    return inner()


a = func()
