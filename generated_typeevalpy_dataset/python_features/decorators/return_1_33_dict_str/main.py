# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return {'jsoir': 53, 'amyit': 6, 'legzf': 27}

    return dec


@func1()
def func2():
    return 'anoza'


a = func2()
