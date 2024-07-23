# Nested functions: defining a function inside another function


def outer():
    x = 'qfkrw'

    def inner():
        nonlocal x
        x += 'qfkrw'
        return x

    return inner()


a = outer()
