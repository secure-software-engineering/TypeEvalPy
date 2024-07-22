#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 65:
            return 'rzast'
        case 'rzast':
            return 65
        case _:
            return "default"


a = func(65)
b = func('rzast')
c = func(33.81)
