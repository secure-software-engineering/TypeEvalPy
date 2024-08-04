#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [31, 84, 75]:
            return 58
        case 58:
            return [31, 84, 75]
        case _:
            return "default"


a = func([31, 84, 75])
b = func(58)
c = func('nxfmb')
