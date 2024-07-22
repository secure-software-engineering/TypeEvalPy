#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 14.7:
            return {'clazc': 16, 'pidpl': 80, 'mlmfg': 53}
        case {'clazc': 16, 'pidpl': 80, 'mlmfg': 53}:
            return 14.7
        case _:
            return "default"


a = func(14.7)
b = func({'clazc': 16, 'pidpl': 80, 'mlmfg': 53})
c = func(False)
