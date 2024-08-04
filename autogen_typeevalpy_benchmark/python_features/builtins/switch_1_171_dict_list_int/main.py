#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'ktnnm': 87, 'zzhgx': 80, 'gagyt': 47}:
            return [11, 67, 55]
        case [11, 67, 55]:
            return {'ktnnm': 87, 'zzhgx': 80, 'gagyt': 47}
        case _:
            return "default"


a = func({'ktnnm': 87, 'zzhgx': 80, 'gagyt': 47})
b = func([11, 67, 55])
c = func(80)
