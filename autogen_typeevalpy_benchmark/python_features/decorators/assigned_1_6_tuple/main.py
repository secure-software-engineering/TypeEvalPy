# A decorator as a variable that has been assigned to function(s).


def dec1(f):
    def wrapper(a, b):
        result = f(a, b)
        return result

    return wrapper


a = dec1


@a
def func(a, b):
    return a + b


c = func((46, 95, 22), (46, 95, 22))
