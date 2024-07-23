#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (39, 45, 57):
            return 'ovyix'
        case 'ovyix':
            return (39, 45, 57)
        case _:
            return "default"


a = func((39, 45, 57))
b = func('ovyix')
c = func({'ekbkq': 37, 'jzoxs': 15, 'mblgg': 32})
