# Call of a function which was yielded.


def func2():
    return 5


def func1(n):
    num = 0
    while num < n:
        yield func2
        num += 1


for i in func1(10):
    try:
        a += i()
    except NameError:
        a = i()
