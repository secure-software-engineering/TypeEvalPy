# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 42

    return dec


@func1()
def func2():
    return "Hello from func2"


a = func2()
