#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [52, 99, 63]:
            return 'dbizh'
        case 'dbizh':
            return [52, 99, 63]
        case _:
            return "default"


a = func([52, 99, 63])
b = func('dbizh')
c = func(89)
