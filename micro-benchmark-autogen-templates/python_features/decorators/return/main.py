# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return <value1>

    return dec


@func1()
def func2():
    return <value2>


a = func2()
