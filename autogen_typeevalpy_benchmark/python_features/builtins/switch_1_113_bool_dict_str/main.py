#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return {'huiai': 31, 'epuje': 50, 'vvfsq': 1}
        case {'huiai': 31, 'epuje': 50, 'vvfsq': 1}:
            return False
        case _:
            return "default"


a = func(False)
b = func({'huiai': 31, 'epuje': 50, 'vvfsq': 1})
c = func('opszi')
