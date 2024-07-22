#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return {'zosll': 96, 'hpugy': 35, 'sdpnd': 62}
        case {'zosll': 96, 'hpugy': 35, 'sdpnd': 62}:
            return True
        case _:
            return "default"


a = func(True)
b = func({'zosll': 96, 'hpugy': 35, 'sdpnd': 62})
c = func((49, 8, 41))
