#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 83:
            return (39, 90, 40)
        case (39, 90, 40):
            return 83
        case _:
            return "default"


a = func(83)
b = func((39, 90, 40))
c = func({'lznnk': 78, 'qorde': 14, 'udrlr': 54})
