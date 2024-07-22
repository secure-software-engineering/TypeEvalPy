#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 15.66:
            return {'smbtc': 47, 'qyltt': 25, 'givmo': 87}
        case {'smbtc': 47, 'qyltt': 25, 'givmo': 87}:
            return 15.66
        case _:
            return "default"


a = func(15.66)
b = func({'smbtc': 47, 'qyltt': 25, 'givmo': 87})
c = func('lhwin')
