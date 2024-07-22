#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [85, 58, 90]:
            return False
        case False:
            return [85, 58, 90]
        case _:
            return "default"


a = func([85, 58, 90])
b = func(False)
c = func({'dzcln': 47, 'mbhko': 76, 'blwoh': 68})
