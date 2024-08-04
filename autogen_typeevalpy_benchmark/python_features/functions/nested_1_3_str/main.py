# Nested functions: defining a function inside another function


def outer():
    x = 'xeadt'

    def inner():
        nonlocal x
        x += 'xeadt'
        return x

    return inner()


a = outer()
