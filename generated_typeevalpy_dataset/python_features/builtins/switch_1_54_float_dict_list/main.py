#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 57.2:
            return {'kiexc': 3, 'oruqw': 6, 'neqfm': 77}
        case {'kiexc': 3, 'oruqw': 6, 'neqfm': 77}:
            return 57.2
        case _:
            return "default"


a = func(57.2)
b = func({'kiexc': 3, 'oruqw': 6, 'neqfm': 77})
c = func([70, 84, 60])
