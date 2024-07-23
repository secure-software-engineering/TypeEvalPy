# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return {'xhshq': 33, 'qldjk': 34, 'bksan': 37}

    @dec
    def inner():
        return False

    return inner()


a = func()
