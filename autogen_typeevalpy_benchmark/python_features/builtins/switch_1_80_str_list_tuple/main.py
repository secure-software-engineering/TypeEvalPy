#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'xtgwv':
            return [72, 60, 66]
        case [72, 60, 66]:
            return 'xtgwv'
        case _:
            return "default"


a = func('xtgwv')
b = func([72, 60, 66])
c = func((36, 29, 50))
