# Nested functions: defining a function inside another function


def outer():
    x = 61.99

    def inner():
        nonlocal x
        x += 61.99
        return x

    return inner()


a = outer()
