#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 35:
            return {'dffkt': 83, 'anzpx': 79, 'iltid': 13}
        case {'dffkt': 83, 'anzpx': 79, 'iltid': 13}:
            return 35
        case _:
            return "default"


a = func(35)
b = func({'dffkt': 83, 'anzpx': 79, 'iltid': 13})
c = func([86, 48, 94])
