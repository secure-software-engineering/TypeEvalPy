#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (29, 68, 27):
            return {'iejhw': 3, 'idfgl': 29, 'cprzz': 16}
        case {'iejhw': 3, 'idfgl': 29, 'cprzz': 16}:
            return (29, 68, 27)
        case _:
            return "default"


a = func((29, 68, 27))
b = func({'iejhw': 3, 'idfgl': 29, 'cprzz': 16})
c = func([86, 63, 78])
