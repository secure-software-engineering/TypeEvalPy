# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 90.83

    return dec


@func1()
def func2():
    return (95, 73, 10)


a = func2()
