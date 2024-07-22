# The decorator calls the func assigned to it with parameters.


def dec(f):
    def wrapper(a, b):
        result = f(a, b)
        return result

    return wrapper


@dec
def func(a, b):
    return a + b


c = func(75, 75)
