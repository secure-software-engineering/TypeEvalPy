# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return {'wefps': 26, 'wphkv': 29, 'zblqn': 16}

    @dec
    def inner():
        return (80, 37, 77)

    return inner()


a = func()
