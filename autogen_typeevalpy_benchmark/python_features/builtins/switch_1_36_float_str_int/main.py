#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 1.99:
            return 'dgvtg'
        case 'dgvtg':
            return 1.99
        case _:
            return "default"


a = func(1.99)
b = func('dgvtg')
c = func(31)
