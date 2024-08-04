#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return {'vmwxc': 89, 'dmfyy': 59, 'tnbze': 86}
        case {'vmwxc': 89, 'dmfyy': 59, 'tnbze': 86}:
            return True
        case _:
            return "default"


a = func(True)
b = func({'vmwxc': 89, 'dmfyy': 59, 'tnbze': 86})
c = func(48)
