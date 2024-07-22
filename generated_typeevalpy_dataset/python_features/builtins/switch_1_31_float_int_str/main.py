#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 96.45:
            return 81
        case 81:
            return 96.45
        case _:
            return "default"


a = func(96.45)
b = func(81)
c = func('whsiv')
