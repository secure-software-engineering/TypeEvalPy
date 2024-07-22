# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return [30, 11, 80]

    return dec


@func1()
def func2():
    return {'jpype': 94, 'mazgh': 35, 'pnsqc': 91}


a = func2()
