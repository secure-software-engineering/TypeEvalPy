# Nested functions: defining a function inside another function


def outer():
    x = 6

    def inner():
        nonlocal x
        x += 6
        return x

    return inner()


a = outer()
