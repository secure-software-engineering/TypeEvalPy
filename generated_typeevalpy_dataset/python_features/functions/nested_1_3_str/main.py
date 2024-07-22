# Nested functions: defining a function inside another function


def outer():
    x = 'oawco'

    def inner():
        nonlocal x
        x += 'oawco'
        return x

    return inner()


a = outer()
