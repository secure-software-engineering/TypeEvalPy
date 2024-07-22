# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return {'nkolp': 41, 'ugvdc': 100, 'mvwzs': 30}

    @dec
    def inner():
        return [87, 18, 94]

    return inner()


a = func()
