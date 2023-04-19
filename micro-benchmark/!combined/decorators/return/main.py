# The decorator is a function call.


def func1():
    def dec(f):
        return f

    return dec


@func1()
def func2():
    return "Hello from func2"


a = func2()