#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return [56, 85, 62]
        case [56, 85, 62]:
            return False
        case _:
            return "default"


a = func(False)
b = func([56, 85, 62])
c = func({'cdpvi': 81, 'zbzsx': 32, 'kbxcy': 18})
