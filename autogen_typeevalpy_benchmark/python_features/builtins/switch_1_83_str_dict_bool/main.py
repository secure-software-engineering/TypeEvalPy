#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'dvgqc':
            return {'vxqaa': 83, 'ctqfu': 55, 'jdbrg': 57}
        case {'vxqaa': 83, 'ctqfu': 55, 'jdbrg': 57}:
            return 'dvgqc'
        case _:
            return "default"


a = func('dvgqc')
b = func({'vxqaa': 83, 'ctqfu': 55, 'jdbrg': 57})
c = func(True)
