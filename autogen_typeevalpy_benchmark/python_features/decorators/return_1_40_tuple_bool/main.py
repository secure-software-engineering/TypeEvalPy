# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return (66, 29, 7)

    return dec


@func1()
def func2():
    return True


a = func2()
