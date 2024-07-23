#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'ljkfl': 17, 'jekuv': 76, 'snocb': 59}:
            return 86
        case 86:
            return {'ljkfl': 17, 'jekuv': 76, 'snocb': 59}
        case _:
            return "default"


a = func({'ljkfl': 17, 'jekuv': 76, 'snocb': 59})
b = func(86)
c = func(57.87)
