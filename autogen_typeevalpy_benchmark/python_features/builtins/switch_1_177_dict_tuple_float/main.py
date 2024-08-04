#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'bgzsa': 4, 'wyfqo': 48, 'cvejr': 77}:
            return (91, 28, 23)
        case (91, 28, 23):
            return {'bgzsa': 4, 'wyfqo': 48, 'cvejr': 77}
        case _:
            return "default"


a = func({'bgzsa': 4, 'wyfqo': 48, 'cvejr': 77})
b = func((91, 28, 23))
c = func(27.26)
