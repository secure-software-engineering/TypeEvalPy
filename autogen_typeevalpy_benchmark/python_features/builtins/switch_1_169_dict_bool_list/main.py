#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'mdzlc': 96, 'gobea': 6, 'hmdep': 78}:
            return True
        case True:
            return {'mdzlc': 96, 'gobea': 6, 'hmdep': 78}
        case _:
            return "default"


a = func({'mdzlc': 96, 'gobea': 6, 'hmdep': 78})
b = func(True)
c = func([99, 5, 46])
