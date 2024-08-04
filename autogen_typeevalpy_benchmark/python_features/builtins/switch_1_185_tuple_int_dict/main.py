#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (42, 92, 1):
            return 11
        case 11:
            return (42, 92, 1)
        case _:
            return "default"


a = func((42, 92, 1))
b = func(11)
c = func({'meeqz': 21, 'gsood': 9, 'rxdjc': 25})
