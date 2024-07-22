#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (96, 59, 88):
            return [88, 64, 88]
        case [88, 64, 88]:
            return (96, 59, 88)
        case _:
            return "default"


a = func((96, 59, 88))
b = func([88, 64, 88])
c = func({'rnsip': 82, 'jehya': 87, 'hgegp': 91})
