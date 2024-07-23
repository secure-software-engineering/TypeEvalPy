#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return {'xdwqb': 71, 'yyfyd': 72, 'ntoff': 91}
        case {'xdwqb': 71, 'yyfyd': 72, 'ntoff': 91}:
            return False
        case _:
            return "default"


a = func(False)
b = func({'xdwqb': 71, 'yyfyd': 72, 'ntoff': 91})
c = func([92, 62, 52])
