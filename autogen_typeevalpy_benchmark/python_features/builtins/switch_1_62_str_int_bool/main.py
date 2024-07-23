#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'hecbn':
            return 62
        case 62:
            return 'hecbn'
        case _:
            return "default"


a = func('hecbn')
b = func(62)
c = func(True)
