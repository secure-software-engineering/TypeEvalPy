#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (39, 34, 88):
            return [73, 93, 85]
        case [73, 93, 85]:
            return (39, 34, 88)
        case _:
            return "default"


a = func((39, 34, 88))
b = func([73, 93, 85])
c = func('sllwk')
