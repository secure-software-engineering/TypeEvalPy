#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (90, 14, 42):
            return 53.38
        case 53.38:
            return (90, 14, 42)
        case _:
            return "default"


a = func((90, 14, 42))
b = func(53.38)
c = func('lbocz')
