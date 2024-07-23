#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (33, 35, 96):
            return 'smanc'
        case 'smanc':
            return (33, 35, 96)
        case _:
            return "default"


a = func((33, 35, 96))
b = func('smanc')
c = func(True)
