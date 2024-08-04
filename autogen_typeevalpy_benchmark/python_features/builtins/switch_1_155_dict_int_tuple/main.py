#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'mjttf': 39, 'wynwq': 26, 'wpmdh': 12}:
            return 4
        case 4:
            return {'mjttf': 39, 'wynwq': 26, 'wpmdh': 12}
        case _:
            return "default"


a = func({'mjttf': 39, 'wynwq': 26, 'wpmdh': 12})
b = func(4)
c = func((80, 2, 60))
