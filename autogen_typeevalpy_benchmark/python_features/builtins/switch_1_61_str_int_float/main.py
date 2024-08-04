#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'shdbj':
            return 6
        case 6:
            return 'shdbj'
        case _:
            return "default"


a = func('shdbj')
b = func(6)
c = func(80.67)
