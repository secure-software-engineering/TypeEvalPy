# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return 69.09

    @dec
    def inner():
        return {'kkshi': 68, 'qwmrf': 23, 'amovf': 83}

    return inner()


a = func()
