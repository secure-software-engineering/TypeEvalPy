#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'avolj': 61, 'wxsyh': 29, 'xoafa': 89}:
            return 69.99
        case 69.99:
            return {'avolj': 61, 'wxsyh': 29, 'xoafa': 89}
        case _:
            return "default"


a = func({'avolj': 61, 'wxsyh': 29, 'xoafa': 89})
b = func(69.99)
c = func('lncti')
