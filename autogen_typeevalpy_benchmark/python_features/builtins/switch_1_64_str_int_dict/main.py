#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'rdgyl':
            return 89
        case 89:
            return 'rdgyl'
        case _:
            return "default"


a = func('rdgyl')
b = func(89)
c = func({'mrmub': 95, 'ntxop': 57, 'mowll': 48})
