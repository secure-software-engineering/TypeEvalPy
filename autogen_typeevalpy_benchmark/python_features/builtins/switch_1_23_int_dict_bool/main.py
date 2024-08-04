#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 51:
            return {'edgtc': 86, 'exeqm': 11, 'kjbpl': 68}
        case {'edgtc': 86, 'exeqm': 11, 'kjbpl': 68}:
            return 51
        case _:
            return "default"


a = func(51)
b = func({'edgtc': 86, 'exeqm': 11, 'kjbpl': 68})
c = func(False)
