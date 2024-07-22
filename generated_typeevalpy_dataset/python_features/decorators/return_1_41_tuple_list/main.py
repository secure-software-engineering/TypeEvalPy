# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return (35, 93, 18)

    return dec


@func1()
def func2():
    return [10, 3, 66]


a = func2()
