# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return (26, 79, 49)

    @dec
    def inner():
        return {'xgscs': 52, 'iddgm': 10, 'wokcb': 61}

    return inner()


a = func()
