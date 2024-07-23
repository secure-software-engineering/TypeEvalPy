# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return {'olxuu': 64, 'rssqy': 55, 'metvg': 3}

    @dec
    def inner():
        return 10

    return inner()


a = func()
