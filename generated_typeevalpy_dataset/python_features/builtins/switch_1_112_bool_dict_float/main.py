#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return {'xhsjg': 9, 'dzrib': 22, 'fxocr': 75}
        case {'xhsjg': 9, 'dzrib': 22, 'fxocr': 75}:
            return True
        case _:
            return "default"


a = func(True)
b = func({'xhsjg': 9, 'dzrib': 22, 'fxocr': 75})
c = func(44.46)
