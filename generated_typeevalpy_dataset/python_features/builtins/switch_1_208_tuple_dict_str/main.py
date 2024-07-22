#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (54, 1, 39):
            return {'cmhuh': 68, 'vuzhe': 67, 'tdtez': 32}
        case {'cmhuh': 68, 'vuzhe': 67, 'tdtez': 32}:
            return (54, 1, 39)
        case _:
            return "default"


a = func((54, 1, 39))
b = func({'cmhuh': 68, 'vuzhe': 67, 'tdtez': 32})
c = func('echdb')
