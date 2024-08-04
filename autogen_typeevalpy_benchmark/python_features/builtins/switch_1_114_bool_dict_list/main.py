#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return {'maytd': 44, 'falql': 1, 'qnuir': 76}
        case {'maytd': 44, 'falql': 1, 'qnuir': 76}:
            return True
        case _:
            return "default"


a = func(True)
b = func({'maytd': 44, 'falql': 1, 'qnuir': 76})
c = func([44, 74, 97])
