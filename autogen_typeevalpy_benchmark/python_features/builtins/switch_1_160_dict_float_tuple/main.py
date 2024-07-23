#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'qsavk': 95, 'lftav': 25, 'uyvuh': 24}:
            return 57.2
        case 57.2:
            return {'qsavk': 95, 'lftav': 25, 'uyvuh': 24}
        case _:
            return "default"


a = func({'qsavk': 95, 'lftav': 25, 'uyvuh': 24})
b = func(57.2)
c = func((14, 76, 39))
