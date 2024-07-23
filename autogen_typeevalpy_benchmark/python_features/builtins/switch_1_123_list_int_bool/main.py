#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [65, 99, 72]:
            return 46
        case 46:
            return [65, 99, 72]
        case _:
            return "default"


a = func([65, 99, 72])
b = func(46)
c = func(False)
