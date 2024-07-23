# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return {'teisn': 64, 'cwbml': 82, 'kbsjo': 54}

    return dec


@func1()
def func2():
    return (90, 44, 37)


a = func2()
