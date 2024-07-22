#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'mhkys':
            return False
        case False:
            return 'mhkys'
        case _:
            return "default"


a = func('mhkys')
b = func(False)
c = func({'ecxya': 41, 'zmicq': 8, 'cjonf': 13})
