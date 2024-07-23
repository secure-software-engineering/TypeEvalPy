#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 79.44:
            return False
        case False:
            return 79.44
        case _:
            return "default"


a = func(79.44)
b = func(False)
c = func({'apptc': 35, 'qlupn': 82, 'xgnet': 57})
