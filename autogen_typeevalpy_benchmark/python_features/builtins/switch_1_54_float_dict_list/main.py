#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 14.85:
            return {'cbunq': 10, 'stjwr': 21, 'twidv': 57}
        case {'cbunq': 10, 'stjwr': 21, 'twidv': 57}:
            return 14.85
        case _:
            return "default"


a = func(14.85)
b = func({'cbunq': 10, 'stjwr': 21, 'twidv': 57})
c = func([96, 41, 75])
