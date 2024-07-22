#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 38.44:
            return [96, 96, 41]
        case [96, 96, 41]:
            return 38.44
        case _:
            return "default"


a = func(38.44)
b = func([96, 96, 41])
c = func('ihinr')
