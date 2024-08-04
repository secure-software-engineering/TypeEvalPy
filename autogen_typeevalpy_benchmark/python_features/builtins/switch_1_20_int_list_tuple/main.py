#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 51:
            return [7, 83, 12]
        case [7, 83, 12]:
            return 51
        case _:
            return "default"


a = func(51)
b = func([7, 83, 12])
c = func((53, 37, 88))
