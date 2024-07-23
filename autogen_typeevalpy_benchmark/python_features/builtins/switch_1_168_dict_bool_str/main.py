#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'frtmt': 99, 'szbnr': 36, 'xjyde': 77}:
            return True
        case True:
            return {'frtmt': 99, 'szbnr': 36, 'xjyde': 77}
        case _:
            return "default"


a = func({'frtmt': 99, 'szbnr': 36, 'xjyde': 77})
b = func(True)
c = func('fbrtj')
