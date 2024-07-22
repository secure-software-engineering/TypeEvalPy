#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (71, 44, 56):
            return {'dsfqr': 88, 'khkjr': 84, 'ociwe': 86}
        case {'dsfqr': 88, 'khkjr': 84, 'ociwe': 86}:
            return (71, 44, 56)
        case _:
            return "default"


a = func((71, 44, 56))
b = func({'dsfqr': 88, 'khkjr': 84, 'ociwe': 86})
c = func(False)
