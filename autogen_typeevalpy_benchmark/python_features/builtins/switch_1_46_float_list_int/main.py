#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 66.4:
            return [64, 93, 89]
        case [64, 93, 89]:
            return 66.4
        case _:
            return "default"


a = func(66.4)
b = func([64, 93, 89])
c = func(88)
