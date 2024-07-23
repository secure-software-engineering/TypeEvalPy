#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [93, 55, 73]:
            return {'qliic': 8, 'irgsy': 24, 'yzxtm': 34}
        case {'qliic': 8, 'irgsy': 24, 'yzxtm': 34}:
            return [93, 55, 73]
        case _:
            return "default"


a = func([93, 55, 73])
b = func({'qliic': 8, 'irgsy': 24, 'yzxtm': 34})
c = func((53, 92, 41))
