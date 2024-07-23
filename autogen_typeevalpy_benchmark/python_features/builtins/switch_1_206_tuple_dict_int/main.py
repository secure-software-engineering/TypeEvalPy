#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (55, 29, 79):
            return {'dexmw': 70, 'itlcg': 73, 'ptkkb': 4}
        case {'dexmw': 70, 'itlcg': 73, 'ptkkb': 4}:
            return (55, 29, 79)
        case _:
            return "default"


a = func((55, 29, 79))
b = func({'dexmw': 70, 'itlcg': 73, 'ptkkb': 4})
c = func(77)
