#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'qemej': 53, 'tduui': 70, 'tegys': 92}:
            return True
        case True:
            return {'qemej': 53, 'tduui': 70, 'tegys': 92}
        case _:
            return "default"


a = func({'qemej': 53, 'tduui': 70, 'tegys': 92})
b = func(True)
c = func([61, 8, 94])
