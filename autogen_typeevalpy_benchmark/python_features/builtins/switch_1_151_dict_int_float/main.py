#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'msefu': 78, 'rndnj': 7, 'dzllo': 12}:
            return 1
        case 1:
            return {'msefu': 78, 'rndnj': 7, 'dzllo': 12}
        case _:
            return "default"


a = func({'msefu': 78, 'rndnj': 7, 'dzllo': 12})
b = func(1)
c = func(13.98)
