#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (35, 70, 46):
            return 93.98
        case 93.98:
            return (35, 70, 46)
        case _:
            return "default"


a = func((35, 70, 46))
b = func(93.98)
c = func({'woxoy': 88, 'qcxug': 11, 'btpih': 32})
