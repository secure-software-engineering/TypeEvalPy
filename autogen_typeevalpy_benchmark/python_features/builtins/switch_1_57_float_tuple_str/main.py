#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 17.08:
            return (63, 48, 24)
        case (63, 48, 24):
            return 17.08
        case _:
            return "default"


a = func(17.08)
b = func((63, 48, 24))
c = func('gvdmd')
