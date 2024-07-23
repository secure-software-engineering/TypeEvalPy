#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'jzwun': 19, 'iymru': 48, 'pmjfn': 21}:
            return [14, 56, 35]
        case [14, 56, 35]:
            return {'jzwun': 19, 'iymru': 48, 'pmjfn': 21}
        case _:
            return "default"


a = func({'jzwun': 19, 'iymru': 48, 'pmjfn': 21})
b = func([14, 56, 35])
c = func(44)
