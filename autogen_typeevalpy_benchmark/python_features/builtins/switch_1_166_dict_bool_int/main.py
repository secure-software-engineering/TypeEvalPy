#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'cuepd': 12, 'aujti': 92, 'zedpj': 87}:
            return False
        case False:
            return {'cuepd': 12, 'aujti': 92, 'zedpj': 87}
        case _:
            return "default"


a = func({'cuepd': 12, 'aujti': 92, 'zedpj': 87})
b = func(False)
c = func(73)
