#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (30, 97, 81):
            return {'qsswn': 35, 'nwqzl': 60, 'znxam': 4}
        case {'qsswn': 35, 'nwqzl': 60, 'znxam': 4}:
            return (30, 97, 81)
        case _:
            return "default"


a = func((30, 97, 81))
b = func({'qsswn': 35, 'nwqzl': 60, 'znxam': 4})
c = func(21.35)
