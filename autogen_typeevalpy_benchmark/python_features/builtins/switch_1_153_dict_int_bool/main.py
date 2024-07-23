#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'tgmlx': 29, 'scfsb': 98, 'ngexb': 45}:
            return 56
        case 56:
            return {'tgmlx': 29, 'scfsb': 98, 'ngexb': 45}
        case _:
            return "default"


a = func({'tgmlx': 29, 'scfsb': 98, 'ngexb': 45})
b = func(56)
c = func(False)
