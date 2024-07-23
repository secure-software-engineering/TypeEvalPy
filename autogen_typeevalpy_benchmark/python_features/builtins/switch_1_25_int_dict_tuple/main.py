#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 72:
            return {'gjugf': 98, 'qpgjh': 31, 'thwum': 79}
        case {'gjugf': 98, 'qpgjh': 31, 'thwum': 79}:
            return 72
        case _:
            return "default"


a = func(72)
b = func({'gjugf': 98, 'qpgjh': 31, 'thwum': 79})
c = func((81, 41, 67))
