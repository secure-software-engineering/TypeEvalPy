#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'svimh':
            return (8, 31, 36)
        case (8, 31, 36):
            return 'svimh'
        case _:
            return "default"


a = func('svimh')
b = func((8, 31, 36))
c = func(55.18)
