# Nested functions: defining a function inside another function


def outer():
    x = <value1>

    def inner():
        nonlocal x
        x += <value1>
        return x

    return inner()


a = outer()
