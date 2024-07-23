#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 67.84:
            return 'bbjru'
        case 'bbjru':
            return 67.84
        case _:
            return "default"


a = func(67.84)
b = func('bbjru')
c = func({'nyiyi': 23, 'trzsh': 100, 'disvp': 16})
