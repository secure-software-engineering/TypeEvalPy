#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return {'oudfv': 26, 'vxxnm': 2, 'jllqf': 71}
        case {'oudfv': 26, 'vxxnm': 2, 'jllqf': 71}:
            return False
        case _:
            return "default"


a = func(False)
b = func({'oudfv': 26, 'vxxnm': 2, 'jllqf': 71})
c = func('nblap')
