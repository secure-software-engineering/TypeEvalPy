# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return (84, 3, 22)

    return dec


@func1()
def func2():
    return [36, 70, 30]


a = func2()
