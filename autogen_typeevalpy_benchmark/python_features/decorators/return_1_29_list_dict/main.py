# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return [71, 20, 36]

    return dec


@func1()
def func2():
    return {'zaqms': 53, 'pssez': 12, 'abcbu': 58}


a = func2()
