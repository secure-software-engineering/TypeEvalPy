#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 59.96:
            return (8, 18, 49)
        case (8, 18, 49):
            return 59.96
        case _:
            return "default"


a = func(59.96)
b = func((8, 18, 49))
c = func({'vorgf': 25, 'kwxln': 28, 'nhttc': 88})
