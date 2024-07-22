#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [89, 59, 80]:
            return 66.59
        case 66.59:
            return [89, 59, 80]
        case _:
            return "default"


a = func([89, 59, 80])
b = func(66.59)
c = func((69, 95, 61))
