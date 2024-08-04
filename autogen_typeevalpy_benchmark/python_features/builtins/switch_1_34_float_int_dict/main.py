#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 32.15:
            return 18
        case 18:
            return 32.15
        case _:
            return "default"


a = func(32.15)
b = func(18)
c = func({'fjvne': 23, 'zhoyz': 51, 'sdstg': 62})
