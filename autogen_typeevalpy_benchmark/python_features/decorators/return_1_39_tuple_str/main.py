# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return (7, 33, 85)

    return dec


@func1()
def func2():
    return 'cwztv'


a = func2()
