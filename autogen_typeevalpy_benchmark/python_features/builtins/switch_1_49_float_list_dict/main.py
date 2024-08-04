#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 32.56:
            return [40, 91, 60]
        case [40, 91, 60]:
            return 32.56
        case _:
            return "default"


a = func(32.56)
b = func([40, 91, 60])
c = func({'sjvzz': 52, 'amaox': 26, 'xorpu': 45})
