# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return {'xwwdt': 87, 'mhtru': 71, 'aqesi': 74}

    @dec
    def inner():
        return 51.14

    return inner()


a = func()
