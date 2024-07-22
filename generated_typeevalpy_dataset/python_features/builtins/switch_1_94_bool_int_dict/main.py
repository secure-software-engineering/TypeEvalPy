#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return 99
        case 99:
            return True
        case _:
            return "default"


a = func(True)
b = func(99)
c = func({'wwtpt': 74, 'sizro': 75, 'mejeo': 25})
