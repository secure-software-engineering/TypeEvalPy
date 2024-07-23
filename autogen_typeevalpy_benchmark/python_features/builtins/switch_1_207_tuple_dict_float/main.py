#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (66, 74, 60):
            return {'yrqxx': 94, 'rhokx': 32, 'msikw': 87}
        case {'yrqxx': 94, 'rhokx': 32, 'msikw': 87}:
            return (66, 74, 60)
        case _:
            return "default"


a = func((66, 74, 60))
b = func({'yrqxx': 94, 'rhokx': 32, 'msikw': 87})
c = func(7.73)
