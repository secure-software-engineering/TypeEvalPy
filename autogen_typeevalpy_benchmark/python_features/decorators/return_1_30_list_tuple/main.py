# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return [45, 76, 72]

    return dec


@func1()
def func2():
    return (78, 56, 23)


a = func2()
