# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return [8, 87, 10]

    @dec
    def inner():
        return {'azvxy': 57, 'hbrmq': 19, 'fpzhh': 30}

    return inner()


a = func()
