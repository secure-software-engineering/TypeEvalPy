# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return {'ywtin': 66, 'jyzvf': 56, 'jtuzz': 70}

    @dec
    def inner():
        return 97.05

    return inner()


a = func()
