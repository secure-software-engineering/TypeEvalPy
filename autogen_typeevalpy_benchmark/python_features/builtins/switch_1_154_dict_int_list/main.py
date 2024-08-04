#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'dgnya': 37, 'bmiwt': 68, 'vbhed': 39}:
            return 25
        case 25:
            return {'dgnya': 37, 'bmiwt': 68, 'vbhed': 39}
        case _:
            return "default"


a = func({'dgnya': 37, 'bmiwt': 68, 'vbhed': 39})
b = func(25)
c = func([97, 45, 7])
