# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return True

    @dec
    def inner():
        return {'foero': 95, 'fewkx': 88, 'bnbsb': 7}

    return inner()


a = func()
