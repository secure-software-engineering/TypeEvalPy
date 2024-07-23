#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'rbcbc': 70, 'hzwky': 81, 'ilfbo': 29}:
            return [23, 61, 96]
        case [23, 61, 96]:
            return {'rbcbc': 70, 'hzwky': 81, 'ilfbo': 29}
        case _:
            return "default"


a = func({'rbcbc': 70, 'hzwky': 81, 'ilfbo': 29})
b = func([23, 61, 96])
c = func(94.89)
