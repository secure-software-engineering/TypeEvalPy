#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 17:
            return 'euhze'
        case 'euhze':
            return 17
        case _:
            return "default"


a = func(17)
b = func('euhze')
c = func(False)
