#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'cryiq': 41, 'ayauc': 1, 'nubil': 68}:
            return (34, 65, 41)
        case (34, 65, 41):
            return {'cryiq': 41, 'ayauc': 1, 'nubil': 68}
        case _:
            return "default"


a = func({'cryiq': 41, 'ayauc': 1, 'nubil': 68})
b = func((34, 65, 41))
c = func([21, 71, 38])
