# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return {'jbbwh': 55, 'wmkos': 26, 'rblom': 11}

    @dec
    def inner():
        return 'ixycn'

    return inner()


a = func()
