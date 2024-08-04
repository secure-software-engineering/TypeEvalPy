#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [39, 1, 95]:
            return 'izvld'
        case 'izvld':
            return [39, 1, 95]
        case _:
            return "default"


a = func([39, 1, 95])
b = func('izvld')
c = func((20, 38, 98))
