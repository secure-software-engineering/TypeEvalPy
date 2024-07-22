#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return {'ldhhf': 11, 'sgafp': 81, 'ldeuh': 5}
        case {'ldhhf': 11, 'sgafp': 81, 'ldeuh': 5}:
            return True
        case _:
            return "default"


a = func(True)
b = func({'ldhhf': 11, 'sgafp': 81, 'ldeuh': 5})
c = func([30, 35, 45])
