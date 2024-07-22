# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 'qiybg'

    return dec


@func1()
def func2():
    return (75, 17, 79)


a = func2()
