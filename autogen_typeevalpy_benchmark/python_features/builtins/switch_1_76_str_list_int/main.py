#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'owuve':
            return [95, 21, 91]
        case [95, 21, 91]:
            return 'owuve'
        case _:
            return "default"


a = func('owuve')
b = func([95, 21, 91])
c = func(81)
