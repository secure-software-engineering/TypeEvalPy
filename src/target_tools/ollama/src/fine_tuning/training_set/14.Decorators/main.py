# A simple function with a thisisadecorator.


def thisisadec(x):
    def inner_func():
        return "thisisadec"

    return inner_func


@thisisadec
def justafunc():
    pass


x = justafunc()
