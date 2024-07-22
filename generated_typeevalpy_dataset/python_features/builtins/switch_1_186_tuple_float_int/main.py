#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (52, 85, 87):
            return 85.6
        case 85.6:
            return (52, 85, 87)
        case _:
            return "default"


a = func((52, 85, 87))
b = func(85.6)
c = func(60)
