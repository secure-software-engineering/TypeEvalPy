# Nested functions: defining a function inside another function


def outer():
    x = 20.81

    def inner():
        nonlocal x
        x += 20.81
        return x

    return inner()


a = outer()
