# Nested functions: defining a function inside another function


def outer():
    x = 64

    def inner():
        nonlocal x
        x += 64
        return x

    return inner()


a = outer()
