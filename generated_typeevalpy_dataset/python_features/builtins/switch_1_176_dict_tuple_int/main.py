#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'slevg': 72, 'ullqf': 26, 'dkccd': 33}:
            return (26, 43, 2)
        case (26, 43, 2):
            return {'slevg': 72, 'ullqf': 26, 'dkccd': 33}
        case _:
            return "default"


a = func({'slevg': 72, 'ullqf': 26, 'dkccd': 33})
b = func((26, 43, 2))
c = func(17)
