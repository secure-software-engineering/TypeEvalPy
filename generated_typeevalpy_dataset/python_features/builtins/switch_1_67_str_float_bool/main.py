#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'gzsvu':
            return 98.11
        case 98.11:
            return 'gzsvu'
        case _:
            return "default"


a = func('gzsvu')
b = func(98.11)
c = func(False)
