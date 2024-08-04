#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 25.93:
            return {'mmxdg': 87, 'dwmnv': 23, 'wyzfy': 28}
        case {'mmxdg': 87, 'dwmnv': 23, 'wyzfy': 28}:
            return 25.93
        case _:
            return "default"


a = func(25.93)
b = func({'mmxdg': 87, 'dwmnv': 23, 'wyzfy': 28})
c = func(True)
