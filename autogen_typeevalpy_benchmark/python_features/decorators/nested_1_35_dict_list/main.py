# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return {'mpjst': 77, 'wlicq': 66, 'hyoqc': 84}

    @dec
    def inner():
        return [34, 86, 99]

    return inner()


a = func()
