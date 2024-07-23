#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 43:
            return {'dylsf': 68, 'houku': 44, 'asqht': 10}
        case {'dylsf': 68, 'houku': 44, 'asqht': 10}:
            return 43
        case _:
            return "default"


a = func(43)
b = func({'dylsf': 68, 'houku': 44, 'asqht': 10})
c = func('grehq')
