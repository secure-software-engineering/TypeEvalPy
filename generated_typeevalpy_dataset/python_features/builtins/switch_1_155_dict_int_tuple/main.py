#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'wcghi': 13, 'vqymu': 94, 'iextu': 94}:
            return 43
        case 43:
            return {'wcghi': 13, 'vqymu': 94, 'iextu': 94}
        case _:
            return "default"


a = func({'wcghi': 13, 'vqymu': 94, 'iextu': 94})
b = func(43)
c = func((4, 46, 97))
