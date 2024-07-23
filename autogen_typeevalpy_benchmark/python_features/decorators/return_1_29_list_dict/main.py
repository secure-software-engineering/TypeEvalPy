# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return [9, 97, 57]

    return dec


@func1()
def func2():
    return {'orurf': 7, 'kxhsz': 51, 'iyfcc': 13}


a = func2()
