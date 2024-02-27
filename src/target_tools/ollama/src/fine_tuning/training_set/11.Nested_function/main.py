def outer():
    x = 1

    def inner():
        y = "Hello"
        return y

    return inner()


result1 = outer()
