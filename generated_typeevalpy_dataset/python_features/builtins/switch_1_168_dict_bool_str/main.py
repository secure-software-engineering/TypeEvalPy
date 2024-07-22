#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'rkuls': 49, 'qhptf': 42, 'volhj': 99}:
            return False
        case False:
            return {'rkuls': 49, 'qhptf': 42, 'volhj': 99}
        case _:
            return "default"


a = func({'rkuls': 49, 'qhptf': 42, 'volhj': 99})
b = func(False)
c = func('pftnp')
