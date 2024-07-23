#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [92, 54, 78]:
            return {'ddqic': 75, 'mfinp': 24, 'cfouq': 21}
        case {'ddqic': 75, 'mfinp': 24, 'cfouq': 21}:
            return [92, 54, 78]
        case _:
            return "default"


a = func([92, 54, 78])
b = func({'ddqic': 75, 'mfinp': 24, 'cfouq': 21})
c = func(44.16)
