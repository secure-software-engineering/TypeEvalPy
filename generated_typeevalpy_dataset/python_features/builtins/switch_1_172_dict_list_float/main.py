#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'vpina': 28, 'vxnze': 8, 'xtrzu': 34}:
            return [71, 77, 28]
        case [71, 77, 28]:
            return {'vpina': 28, 'vxnze': 8, 'xtrzu': 34}
        case _:
            return "default"


a = func({'vpina': 28, 'vxnze': 8, 'xtrzu': 34})
b = func([71, 77, 28])
c = func(41.38)
