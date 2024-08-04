# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return {'oumol': 93, 'yeaff': 67, 'akgru': 6}

    return dec


@func1()
def func2():
    return [40, 67, 22]


a = func2()
