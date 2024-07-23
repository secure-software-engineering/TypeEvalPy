#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 40:
            return (85, 3, 82)
        case (85, 3, 82):
            return 40
        case _:
            return "default"


a = func(40)
b = func((85, 3, 82))
c = func({'grcjn': 78, 'tjgiw': 32, 'jrvqp': 23})
