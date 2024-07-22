# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 91.9

    return dec


@func1()
def func2():
    return {'kmfyv': 68, 'grovj': 32, 'fzytq': 46}


a = func2()
