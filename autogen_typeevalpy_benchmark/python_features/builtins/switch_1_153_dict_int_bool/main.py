#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'jvvsk': 37, 'eaklf': 25, 'upzjn': 94}:
            return 17
        case 17:
            return {'jvvsk': 37, 'eaklf': 25, 'upzjn': 94}
        case _:
            return "default"


a = func({'jvvsk': 37, 'eaklf': 25, 'upzjn': 94})
b = func(17)
c = func(False)
