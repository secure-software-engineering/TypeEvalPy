#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (46, 79, 35):
            return {'ofmwn': 80, 'hgluh': 9, 'atdnl': 89}
        case {'ofmwn': 80, 'hgluh': 9, 'atdnl': 89}:
            return (46, 79, 35)
        case _:
            return "default"


a = func((46, 79, 35))
b = func({'ofmwn': 80, 'hgluh': 9, 'atdnl': 89})
c = func([8, 3, 98])
