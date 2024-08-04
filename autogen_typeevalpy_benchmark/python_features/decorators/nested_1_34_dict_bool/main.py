# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return {'xadaa': 18, 'hdlku': 56, 'gvqtk': 87}

    @dec
    def inner():
        return False

    return inner()


a = func()
