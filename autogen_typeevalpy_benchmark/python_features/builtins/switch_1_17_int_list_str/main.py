#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 2:
            return [64, 45, 80]
        case [64, 45, 80]:
            return 2
        case _:
            return "default"


a = func(2)
b = func([64, 45, 80])
c = func('ibgty')
