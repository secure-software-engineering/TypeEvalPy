# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return {'jjlve': 2, 'maxqf': 77, 'yrgfz': 52}

    @dec
    def inner():
        return (28, 96, 95)

    return inner()


a = func()
