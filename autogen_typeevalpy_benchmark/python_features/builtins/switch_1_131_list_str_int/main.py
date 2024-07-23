#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [60, 77, 18]:
            return 'rlzfh'
        case 'rlzfh':
            return [60, 77, 18]
        case _:
            return "default"


a = func([60, 77, 18])
b = func('rlzfh')
c = func(24)
