# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return {'ymkus': 10, 'neuug': 60, 'heywr': 16}

    return dec


@func1()
def func2():
    return (5, 25, 81)


a = func2()
