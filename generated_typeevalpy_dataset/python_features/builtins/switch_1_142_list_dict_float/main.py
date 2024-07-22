#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [45, 96, 60]:
            return {'lioqu': 47, 'xulmp': 85, 'dkohh': 11}
        case {'lioqu': 47, 'xulmp': 85, 'dkohh': 11}:
            return [45, 96, 60]
        case _:
            return "default"


a = func([45, 96, 60])
b = func({'lioqu': 47, 'xulmp': 85, 'dkohh': 11})
c = func(5.72)
