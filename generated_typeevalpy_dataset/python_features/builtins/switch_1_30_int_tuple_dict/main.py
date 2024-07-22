#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 81:
            return (77, 40, 60)
        case (77, 40, 60):
            return 81
        case _:
            return "default"


a = func(81)
b = func((77, 40, 60))
c = func({'axlne': 56, 'faptp': 7, 'ugstf': 60})
