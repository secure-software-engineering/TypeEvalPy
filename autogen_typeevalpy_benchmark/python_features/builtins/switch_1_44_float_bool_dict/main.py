#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 71.25:
            return True
        case True:
            return 71.25
        case _:
            return "default"


a = func(71.25)
b = func(True)
c = func({'pieoc': 55, 'ounej': 67, 'erevo': 3})
