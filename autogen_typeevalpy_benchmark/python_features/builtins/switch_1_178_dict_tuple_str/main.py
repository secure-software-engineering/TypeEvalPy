#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'lggse': 25, 'cwycz': 74, 'jxwhe': 72}:
            return (60, 11, 24)
        case (60, 11, 24):
            return {'lggse': 25, 'cwycz': 74, 'jxwhe': 72}
        case _:
            return "default"


a = func({'lggse': 25, 'cwycz': 74, 'jxwhe': 72})
b = func((60, 11, 24))
c = func('wynkv')
