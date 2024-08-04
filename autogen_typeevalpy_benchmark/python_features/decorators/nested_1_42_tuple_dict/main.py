# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return (83, 94, 37)

    @dec
    def inner():
        return {'wbzxy': 100, 'dqtsx': 38, 'muuuf': 14}

    return inner()


a = func()
