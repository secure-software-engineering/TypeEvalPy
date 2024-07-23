# Nested functions: defining a function inside another function


def outer():
    x = 55

    def inner():
        nonlocal x
        x += 55
        return x

    return inner()


a = outer()
