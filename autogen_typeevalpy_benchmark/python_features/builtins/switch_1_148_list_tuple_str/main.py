#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [15, 25, 62]:
            return (62, 57, 19)
        case (62, 57, 19):
            return [15, 25, 62]
        case _:
            return "default"


a = func([15, 25, 62])
b = func((62, 57, 19))
c = func('urlrj')
