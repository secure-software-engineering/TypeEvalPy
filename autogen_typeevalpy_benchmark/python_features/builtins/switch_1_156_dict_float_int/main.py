#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'mrers': 17, 'gytmq': 57, 'flilb': 46}:
            return 48.11
        case 48.11:
            return {'mrers': 17, 'gytmq': 57, 'flilb': 46}
        case _:
            return "default"


a = func({'mrers': 17, 'gytmq': 57, 'flilb': 46})
b = func(48.11)
c = func(29)
