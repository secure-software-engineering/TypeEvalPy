#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'oirug': 3, 'jnwii': 52, 'sowzm': 65}:
            return 91.62
        case 91.62:
            return {'oirug': 3, 'jnwii': 52, 'sowzm': 65}
        case _:
            return "default"


a = func({'oirug': 3, 'jnwii': 52, 'sowzm': 65})
b = func(91.62)
c = func(True)
