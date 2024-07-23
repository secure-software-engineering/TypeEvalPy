# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return [52, 4, 34]

    return dec


@func1()
def func2():
    return (22, 22, 44)


a = func2()
