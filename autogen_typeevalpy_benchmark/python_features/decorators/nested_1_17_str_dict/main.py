# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return 'ulvzn'

    @dec
    def inner():
        return {'cbjzh': 97, 'aqihy': 60, 'pbqco': 20}

    return inner()


a = func()
