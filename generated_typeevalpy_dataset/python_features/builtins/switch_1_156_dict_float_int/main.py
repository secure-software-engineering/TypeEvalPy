#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'lkynn': 27, 'kugdt': 86, 'rrwkd': 69}:
            return 59.27
        case 59.27:
            return {'lkynn': 27, 'kugdt': 86, 'rrwkd': 69}
        case _:
            return "default"


a = func({'lkynn': 27, 'kugdt': 86, 'rrwkd': 69})
b = func(59.27)
c = func(66)
