#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return (72, 87, 72)
        case (72, 87, 72):
            return False
        case _:
            return "default"


a = func(False)
b = func((72, 87, 72))
c = func({'rsotw': 59, 'svjih': 83, 'btbqy': 20})
