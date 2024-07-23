#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (4, 41, 25):
            return 71
        case 71:
            return (4, 41, 25)
        case _:
            return "default"


a = func((4, 41, 25))
b = func(71)
c = func({'ddcqh': 99, 'dwpkg': 75, 'xxjon': 79})
