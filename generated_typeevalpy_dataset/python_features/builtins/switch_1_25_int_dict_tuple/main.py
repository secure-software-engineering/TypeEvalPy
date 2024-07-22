#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 10:
            return {'yrnry': 84, 'uxyrb': 7, 'bkynn': 8}
        case {'yrnry': 84, 'uxyrb': 7, 'bkynn': 8}:
            return 10
        case _:
            return "default"


a = func(10)
b = func({'yrnry': 84, 'uxyrb': 7, 'bkynn': 8})
c = func((63, 19, 75))
