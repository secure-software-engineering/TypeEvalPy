#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 65:
            return 'deepr'
        case 'deepr':
            return 65
        case _:
            return "default"


a = func(65)
b = func('deepr')
c = func(True)
