#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'ruefs': 40, 'rmijw': 32, 'gokrp': 13}:
            return [1, 44, 83]
        case [1, 44, 83]:
            return {'ruefs': 40, 'rmijw': 32, 'gokrp': 13}
        case _:
            return "default"


a = func({'ruefs': 40, 'rmijw': 32, 'gokrp': 13})
b = func([1, 44, 83])
c = func((69, 23, 81))
