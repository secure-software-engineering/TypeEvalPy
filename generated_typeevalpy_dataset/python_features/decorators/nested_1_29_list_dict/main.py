# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return [54, 95, 3]

    @dec
    def inner():
        return {'irvdt': 86, 'zrnxg': 50, 'unjmn': 86}

    return inner()


a = func()
