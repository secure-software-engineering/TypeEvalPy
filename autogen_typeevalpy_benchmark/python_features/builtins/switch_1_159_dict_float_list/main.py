#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'locnn': 15, 'lwjac': 71, 'lguqj': 85}:
            return 64.09
        case 64.09:
            return {'locnn': 15, 'lwjac': 71, 'lguqj': 85}
        case _:
            return "default"


a = func({'locnn': 15, 'lwjac': 71, 'lguqj': 85})
b = func(64.09)
c = func([59, 45, 42])
