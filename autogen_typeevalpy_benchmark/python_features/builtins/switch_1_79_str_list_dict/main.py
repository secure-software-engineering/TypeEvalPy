#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'cadmu':
            return [30, 32, 21]
        case [30, 32, 21]:
            return 'cadmu'
        case _:
            return "default"


a = func('cadmu')
b = func([30, 32, 21])
c = func({'iusrf': 77, 'tmdvr': 87, 'uopmx': 8})
