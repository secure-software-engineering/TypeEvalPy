#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 9.34:
            return {'gjzux': 84, 'kuqbt': 25, 'agbjs': 78}
        case {'gjzux': 84, 'kuqbt': 25, 'agbjs': 78}:
            return 9.34
        case _:
            return "default"


a = func(9.34)
b = func({'gjzux': 84, 'kuqbt': 25, 'agbjs': 78})
c = func([5, 3, 81])
