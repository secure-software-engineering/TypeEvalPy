# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 96.87

    return dec


@func1()
def func2():
    return {'ysolt': 23, 'ggqmg': 93, 'sujqs': 86}


a = func2()
