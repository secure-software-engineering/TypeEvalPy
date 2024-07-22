# Nested functions: defining a function inside another function


def outer():
    x = 91.5

    def inner():
        nonlocal x
        x += 91.5
        return x

    return inner()


a = outer()
