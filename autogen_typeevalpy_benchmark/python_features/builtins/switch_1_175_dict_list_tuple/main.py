#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'cumix': 28, 'sasrr': 97, 'qtcmw': 23}:
            return [38, 40, 68]
        case [38, 40, 68]:
            return {'cumix': 28, 'sasrr': 97, 'qtcmw': 23}
        case _:
            return "default"


a = func({'cumix': 28, 'sasrr': 97, 'qtcmw': 23})
b = func([38, 40, 68])
c = func((31, 33, 28))
