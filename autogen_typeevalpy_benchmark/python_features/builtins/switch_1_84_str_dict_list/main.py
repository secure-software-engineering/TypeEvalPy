#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'cctnr':
            return {'jamht': 12, 'sgaxa': 97, 'cjxfx': 93}
        case {'jamht': 12, 'sgaxa': 97, 'cjxfx': 93}:
            return 'cctnr'
        case _:
            return "default"


a = func('cctnr')
b = func({'jamht': 12, 'sgaxa': 97, 'cjxfx': 93})
c = func([67, 18, 54])
