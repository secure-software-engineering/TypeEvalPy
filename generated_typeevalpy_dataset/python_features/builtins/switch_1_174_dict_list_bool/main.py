#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'aegpc': 26, 'khpno': 4, 'tkdde': 58}:
            return [97, 24, 23]
        case [97, 24, 23]:
            return {'aegpc': 26, 'khpno': 4, 'tkdde': 58}
        case _:
            return "default"


a = func({'aegpc': 26, 'khpno': 4, 'tkdde': 58})
b = func([97, 24, 23])
c = func(True)
