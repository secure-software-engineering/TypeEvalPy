# Nested functions: defining a function inside another function


def outer():
    x = 1

    def inner():
        nonlocal x
        x += 1
        return x

    return inner()


a = outer()
